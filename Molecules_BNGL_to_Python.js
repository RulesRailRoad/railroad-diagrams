// Molecules_BNGL_to_Python.js

export function bnglToRailroad(bnglString, displayString = null, changesDict = null, molSiteDict = {}) {
    const MoleculeColor = 'lightgreen';
    const SiteColor = 'lightblue';
    const StateColor = 'khaki';

    const bondAddedNonRev = "nradded";
    const bondRemovedNonRev = "nrbroken";
    const bondAddedRev = "radded";
    const bondRemovedRev = "rbroken";
    const stateChangeUp = "change from bottom state to top state";
    const stateChangeDown = "change from top state to bottom state";

    const molChunks = bnglString.split('.');
    const diagrams = [
        `add(\"${(displayString || bnglString).trim()}\",`,
        "    Diagram("
    ];

    const moleculeCounter = {};

    molChunks.forEach((chunk, idx) => {
        const molMatch = chunk.trim().match(/(\w+)\((.*)\)/);
        if (!molMatch) {
            console.warn("BNGL string format is invalid:", chunk);
            return;
        }

        const [_, moleculeName, siteBlock] = molMatch;
        moleculeCounter[moleculeName] = (moleculeCounter[moleculeName] || 0) + 1;
        const moleculeInstance = `${moleculeName} #${moleculeCounter[moleculeName]}`;

        diagrams.push(`        Terminal(\"${moleculeName}\", box_color=\"${MoleculeColor}\"),`);

        const sites = siteBlock.split(',').map(s => s.trim());

        sites.forEach(site => {
            let bondArg = "";
            let bondNumArg = "";
            let bondTypeArg = "";
            let bondNum = null;
            let siteName = site;
            let states = [];

            if (site.includes('~')) {
                const parts = site.split('~');
                siteName = parts[0];
                states = parts.slice(1);
                const finStates = [];

                states.forEach((state, stateIdx) => {
                    bondArg = "";
                    bondNumArg = "";
                    bondTypeArg = "";
                    let stateName = state;

                    if (state.includes("!")) {
                        const splitState = state.split("!");
                        stateName = splitState[0];
                        bondNum = splitState[1];

                        // Match Python logic: last state with ? gets bottom bind and wrap
                        if (states.length > 1 && stateIdx === states.length - 1 && bondNum === "?") {
                            states[states.length - 1] = stateName;  // Remove bond symbol
                            finStates.push(`NonTerminal(\"${stateName}\", box_color=\"${StateColor}\", bottom_bind=True, wrap=True)`);
                            return; // continue
                        }

                        if (bondNum === "?") {
                            bondArg = ', bottom_bind=True, bottom_bind_color="gray"';
                            bondNumArg = `, bond_num=\"${bondNum}\"`;
                        } else if (bondNum === "+" || /\d+/.test(bondNum)) {
                            bondArg = ', bottom_bind=True';
                            bondNumArg = `, bond_num=\"${bondNum}\"`;
                        }

                        if (changesDict) {
                            const changes = changesDict[`${moleculeInstance}:${siteName}`];
                            if (changes && changes.change.some(c => [bondAddedNonRev, bondRemovedNonRev, bondAddedRev, bondRemovedRev].includes(c))) {
                                const bondChange = changes.change.find(c => [bondAddedNonRev, bondRemovedNonRev, bondAddedRev, bondRemovedRev].includes(c));
                                bondTypeArg = `, bond_type=\"${bondChange}\"`;
                                if (bondNum === "-") {
                                    const numArg = changes.product.split("!")[1];
                                    bondArg = ', bottom_bind=True';
                                    bondNumArg = `, bond_num=\"${numArg}\"`;
                                }
                            }
                        }
                        state = stateName;
                    }

                    if (changesDict) {
                        const changes = changesDict[`${moleculeInstance}:${siteName}`];
                        if (changes && (changes.change.includes(stateChangeUp) || changes.change.includes(stateChangeDown))) {
                            const direction = changes.change.includes(stateChangeDown) ? "down-arrow" : "up-arrow";
                            const reactantState = changes.reactant.split("~").slice(-1)[0].split("!")[0];
                            const productState = changes.product.split("~").slice(-1)[0].split("!")[0];
                            const siteDefs = molSiteDict[moleculeName] || [];

                            let stateList = [];
                            for (const def of siteDefs) {
                                if (def.startsWith(siteName + "~")) {
                                    stateList = def.split("~").slice(1).map(s => s.split("!")[0]);
                                    break;
                                }
                            }
                            const ordered = stateList.filter(s => [reactantState, productState].includes(s));
                            const allStates = ordered.map(s => {
                                const match = s === state ? `${bondArg}${bondNumArg}${bondTypeArg}` : "";
                                return `NonTerminal(\"${s}\", box_color=\"${StateColor}\"${match})`;
                            });
                            finStates.push(`MultipleChoice(0, \"${direction}\", ${allStates.join(", ")})`);
                        } else {
                            finStates.push(`NonTerminal(\"${state}\", box_color=\"${StateColor}\"${bondArg}${bondNumArg}${bondTypeArg})`);
                        }
                    } else {
                        finStates.push(`NonTerminal(\"${state}\", box_color=\"${StateColor}\"${bondArg}${bondNumArg}${bondTypeArg})`);
                    }
                });

                const stateChoices = finStates.join(", ");
                const siteCode = `    Choice(0, Comment(\"    \"), Sequence(Terminal(\"${siteName}\", box_color=\"${SiteColor}\"), Choice(0, Comment(\"    \"), ${stateChoices}))),`;
                diagrams.push(siteCode);
            } else {
                if (siteName.includes("!")) {
                    const [name, bond] = siteName.split("!");
                    siteName = name;
                    bondNum = bond;
                    if (bondNum === "?") {
                        bondArg = ', bottom_bind=True, bottom_bind_color="gray"';
                        bondNumArg = `, bond_num=\"${bondNum}\"`;
                    } else if (bondNum === "+" || /\d+/.test(bondNum)) {
                        bondArg = ', bottom_bind=True';
                        bondNumArg = `, bond_num=\"${bondNum}\"`;
                    }
                }

                if (changesDict) {
                    const changes = changesDict[`${moleculeInstance}:${siteName}`];
                    if (changes && changes.change.some(c => [bondAddedNonRev, bondRemovedNonRev, bondAddedRev, bondRemovedRev].includes(c))) {
                        const bondChange = changes.change.find(c => [bondAddedNonRev, bondRemovedNonRev, bondAddedRev, bondRemovedRev].includes(c));
                        bondTypeArg = `, bond_type=\"${bondChange}\"`;
                        if (bondNum === "-") {
                            const numArg = changes.product.split("!")[1];
                            bondArg = ', bottom_bind=True';
                            bondNumArg = `, bond_num=\"${numArg}\"`;
                        }
                    }
                }

                const siteCode = `    Choice(0, Comment(\"    \"), Terminal(\"${siteName}\", box_color=\"${SiteColor}\"${bondArg}${bondNumArg}${bondTypeArg})),`;
                diagrams.push(siteCode);
            }
        });

        if (idx < molChunks.length - 1) {
            diagrams.push("        EndWhiteSpace(),");
        }
    });

    diagrams.push("    )\n)");
    return diagrams.join("\n") + "\n";
}