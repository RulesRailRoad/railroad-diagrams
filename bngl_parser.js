// bngl_parser.js
import { expandExpr } from './_expanded.js';
import { compareReactions, stateChangeUp, stateChangeDown, bondAddedNonRev, bondRemovedNonRev, bondAddedRev, bondRemovedRev } from './compare_reactions.js';
import { bnglToRailroad } from './Molecules_BNGL_to_Python.js';

const MoleculeColor = 'lightgreen';
const SiteColor = 'lightblue';
const StateColor = 'khaki';

export function joinLines(lines) {
    const joined = [];
    let current = '';
    for (let line of lines) {
        line = line.trim();
        if (line.endsWith('\\')) {
            current += line.slice(0, -1) + ' ';
        } else {
            current += line;
            joined.push(current);
            current = '';
        }
    }
    if (current) joined.push(current);
    return joined;
}

export function moleculeSiteDict(lines) {
    const dict = {};
    for (const line of lines) {
        if (line.startsWith('#') || !line.includes('(')) continue;
        const match = line.match(/(\w+)\((.*?)\)/);
        if (!match) continue;
        const [_, mol, sitesBlock] = match;
        const sites = sitesBlock.split(',').map(s => s.trim()).filter(Boolean);
        dict[mol] = sites;
    }
    return dict;
}

export async function parseBNGLFile(fileText) {
    const lines = joinLines(fileText.split(/\r?\n/).map(l => l.trim()));
    const output = [];

    const getBlockFlexible = (startTokens, endTokens) => {
        let start = -1, end = -1;
        for (let i = 0; i < lines.length; i++) {
            for (const token of startTokens) {
                if (lines[i].toLowerCase().startsWith(token)) {
                    start = i;
                    break;
                }
            }
            if (start !== -1) break;
        }
        for (let i = start + 1; i < lines.length; i++) {
            for (const token of endTokens) {
                if (lines[i].toLowerCase().startsWith(token)) {
                    end = i;
                    break;
                }
            }
            if (end !== -1) break;
        }
        return start !== -1 && end !== -1 ? lines.slice(start + 1, end) : [];
    };

    const moleculeLines = getBlockFlexible(["begin molecule types", "begin molecules"], ["end molecule types", "end molecules"]);
    const molSiteDict = moleculeSiteDict(moleculeLines);

    output.push('sys.stdout.write("<h1>Molecules</h1>\\n")');
    for (const line of moleculeLines) {
        if (!line.startsWith('#')) {
            output.push(bnglToRailroad(line, null, null, molSiteDict));
        }
    }

    const speciesLines = getBlockFlexible(["begin species", "begin seed species"], ["end species", "end seed species"]);
    if (speciesLines.length > 0) {
        output.push('sys.stdout.write("<h1>Species</h1>\\n")');
        for (const line of speciesLines) {
            if (!line || line.startsWith('#')) continue;
            const parts = line.split(/\s+/);
            let species = parts.find(p => p.includes('(') && p.includes(')')) || '';
            if (species.includes(':')) species = species.split(':')[1];
            if (species) output.push(bnglToRailroad(species, null, null, molSiteDict));
        }
    }

    const obsLines = getBlockFlexible(["begin observables"], ["end observables"]);
    if (obsLines.length > 0) {
        output.push('sys.stdout.write("<h1>Observables</h1>\\n")');
        for (const line of obsLines) {
            if (!line || line.startsWith('#')) continue;
            const parts = line.split(/\s+/);
            let expr = parts.slice(2).join(' ');
            if (expr.includes(':')) expr = expr.split(':')[1];
            const expanded = expandExpr(expr, molSiteDict);
            output.push(bnglToRailroad(expanded, expr, null, molSiteDict));
        }
    }

    const reactionLines = getBlockFlexible(["begin reaction"], ["end reaction"]);
    if (reactionLines.length > 0) {
        output.push('sys.stdout.write("<h1>Reactions</h1>\\n")');
        for (let line of reactionLines) {
            if (!line || line.startsWith('#')) continue;

            // Remove rule name and clean up @LOC: labels
            if (line.includes(':')) line = line.split(':', 2)[1].trim();
            line = line.replace(/@[A-Za-z]+:/g, '');

            const arrow = line.includes('<->') ? '<->' : (line.includes('->') ? '->' : null);
            if (!arrow) continue;

            const [lhsRaw, rhsRaw] = line.split(arrow).map(s => s.trim());
            const lhs = lhsRaw.split(/[ \t]/)[0];
            const rhs = rhsRaw.split(/[ \t]/)[0];

            const reactants = lhs.split('+').map(r => r.trim().split(':').pop().split(')')[0] + ')').join(' + ');
            const products = rhs.split('+').map(p => p.trim().split(':').pop().split(')')[0] + ')').join(' + ');

            const expandedLHS = expandExpr(reactants.replace(/ \+ /g, '.'), molSiteDict);
            const expandedRHS = expandExpr(products.replace(/ \+ /g, '.'), molSiteDict);
            const display = `${reactants} ${arrow} ${products}`;

            const changes = compareReactions(expandedLHS, expandedRHS, arrow, molSiteDict);
            output.push(bnglToRailroad(expandedLHS, display, changes, molSiteDict));
        }
    }

    return output.join('\n');
}
