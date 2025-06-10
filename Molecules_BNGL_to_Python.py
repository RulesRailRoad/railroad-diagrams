import re
import sys

MoleculeColor = 'lightgreen'
SiteColor = 'lightblue'
StateColor = 'khaki'

def bngl_to_railroad(bngl_string, display_string=None, changes_dict=None):
    mol_chunks = bngl_string.split('.')
    if display_string:
        diagrams = [f'add("{display_string.strip()}",', "    Diagram("]
    else:
        diagrams = [f'add("{bngl_string.strip()}",', "    Diagram("]

    molecule_counter = {}
    for idx, chunk in enumerate(mol_chunks):
        mol_match = re.match(r"(\w+)\((.*)\)", chunk.strip())
        if not mol_match:
            print("BNGL string format is invalid.")
            continue
        
        molecule_name, site_block = mol_match.groups()
        if molecule_name in molecule_counter:
            molecule_counter[molecule_name] +=1
        else:
            molecule_counter[molecule_name] =1
        molecule_instance = f'{molecule_name} #{molecule_counter[molecule_name]}'
        sites = [s.strip() for s in site_block.split(',')]

        diagrams.append(f'        Terminal("{molecule_name}", box_color="{MoleculeColor}"),')

        # Step 2: Process each site
        for site in sites:
            bond_arg = ""
            bond_num_arg = ""
            bond_type_arg = ""
            bond_num = None

            site_name = site
            states = []
                 
            
            if '~' in site:
                # Split into site name and states
                parts = site.split('~')
                site_name = parts[0]
                states = parts[1:]

                fin_states = []
                for state_idx, state in enumerate(states):
                    bond_arg = ""
                    bond_num_arg = ""
                    bond_type_arg = ""
                    if "!" in state:
                        state_split = state.split("!")
                        state_name = state_split[0]
                        bond_num = state_split[1]
                        
                        if len(states) > 1 and state_idx == len(states)-1 and bond_num == "?":
                            states[-1] = states[-1].split("!")[0]
                            fin_states.append(f'NonTerminal("{state_name}", box_color="{StateColor}", bottom_bind=True, wrap=True)')
                            continue

                        if bond_num == "?":
                            bond_arg = ', bottom_bind=True, bottom_bind_color="gray"'
                            bond_num_arg = f', bond_num="{bond_num}"'
                        elif bond_num == "+":
                            bond_arg = ', bottom_bind=True'
                            bond_num_arg = f', bond_num="{bond_num}"'
                        elif bond_num.isdigit():
                            bond_arg = ', bottom_bind=True'
                            bond_num_arg = f', bond_num="{bond_num}"'
                        if changes_dict:
                            changes = changes_dict.get(f'{molecule_instance}:{site_name}')
                            if changes and any(change in (bond_added_non_rev, bond_removed_non_rev, bond_added_rev, bond_removed_rev) for change in changes["change"]):
                                bond_changes = [bond_added_non_rev, bond_removed_non_rev, bond_added_rev, bond_removed_rev]
                                bond_change = [change for change in changes["change"] if change in bond_changes]
                                bond_type_arg = f', bond_type="{"".join(bond_change)}"'
                                if bond_num == "-":
                                    num_arg = changes["product"].split("!")[1]
                                    bond_arg = ', bottom_bind=True'
                                    bond_num_arg = f', bond_num="{num_arg}"'
                                elif bond_num.isdigit():
                                    bond_arg = ', bottom_bind=True'
                                    bond_num_arg = f', bond_num="{bond_num}"'
                                
                        state = state_name
                    if changes_dict:
                        changes = changes_dict.get(f'{molecule_instance}:{site_name}')
                        if changes and (state_change_up in changes["change"] or state_change_down in changes["change"]):
                            direction = "down-arrow" if (state_change_down in changes["change"]) else "up-arrow"
                            reactant_state = changes["reactant"].split("~")[-1].split("!")[0]
                            product_state = changes["product"].split("~")[-1].split("!")[0]

                            for mol_site in mol_site_dict.get(molecule_name):
                                if mol_site.startswith(site_name) and "~" in mol_site:
                                    state_list = [s.split("!")[0] for s in mol_site.split("~")[1:]]
                                    break
                            ordered_states = [s for s in state_list if s in (reactant_state, product_state)]
                            all_states = []
                            for s in ordered_states:
                                bond_args = ""
                                if s == state:
                                    bond_args = f"{bond_arg}{bond_num_arg}{bond_type_arg}"
                                all_states.append(f'NonTerminal("{s}", box_color="{StateColor}"{bond_args})')
                            fin_states = [f'MultipleChoice(0, "{direction}", {", ".join(all_states)})']
                        else:
                            fin_states.append(f'NonTerminal("{state}", box_color="{StateColor}"{bond_arg}{bond_num_arg}{bond_type_arg})')
                    else:
                            fin_states.append(f'NonTerminal("{state}", box_color="{StateColor}"{bond_arg}{bond_num_arg}{bond_type_arg})')

                state_choices = ', '.join(fin_states)
                site_code = f'''    Choice(0, Comment("    "), Sequence(Terminal("{site_name}", box_color='{SiteColor}'), Choice(0, Comment("    "), {state_choices}))),'''
            else:
                if "!" in site_name:
                    site_split = site_name.split("!")
                    site_name = site_split[0]
                    bond_num = site_split[1]
                    if bond_num == "?":
                        bond_arg = ', bottom_bind=True, bottom_bind_color="gray"'
                        bond_num_arg = f', bond_num="{bond_num}"'
                    elif bond_num == "+":
                        bond_arg = ', bottom_bind=True'
                        bond_num_arg = f', bond_num="{bond_num}"'
                    elif bond_num.isdigit():
                        bond_arg = ', bottom_bind=True'
                        bond_num_arg = f', bond_num="{bond_num}"'

                if changes_dict:
                    changes = changes_dict.get(f'{molecule_instance}:{site_name}')
                    if changes and any(change in (bond_added_non_rev, bond_removed_non_rev, bond_added_rev, bond_removed_rev) for change in changes["change"]):
                        bond_changes = [bond_added_non_rev, bond_removed_non_rev, bond_added_rev, bond_removed_rev]
                        bond_change = [change for change in changes["change"] if change in bond_changes]
                        bond_type_arg = f', bond_type="{"".join(bond_change)}"'
                        if bond_num == "-":
                            num_arg = changes["product"].split("!")[1]
                            bond_arg = ', bottom_bind=True'
                            bond_num_arg = f', bond_num="{num_arg}"'
                        if bond_num.isdigit():
                            bond_arg = ', bottom_bind=True'
                            bond_num_arg = f', bond_num="{bond_num}"'

                        

                site_code = f'''    Choice(0, Comment("    "), Terminal("{site_name}", box_color='{SiteColor}'{bond_arg}{bond_num_arg}{bond_type_arg})),'''
            
            diagrams.append(site_code)
        if idx < len(mol_chunks)-1:
            diagrams.append("        EndWhiteSpace(),")

    diagrams.append("    )\n)")
    return "\n".join(diagrams) + "\n"

def join_lines(lines):
    joined_lines = []
    line_string = ""
    for line in lines:
        line = line.strip()
        if line.endswith("\\"):
            line_string += line[:-1] + " "
        else:
            line_string += line
            joined_lines.append(line_string)
            line_string = ""
    if line_string:
        joined_lines.append(line_string)

    return joined_lines


# take .bngl file as input
filepath = input('BNGL filepath: ')
file = filepath + '.bngl'
with open(file, 'r') as f:
    print('\nOpening file for reading:', file)
    lines = f.readlines()
lines = [line.strip() for line in lines]
lines = join_lines(lines)

output_file = filepath + '_output.py'


# save molecules to dictionary
def molecule_site_dict(molecule_lines):
    mol_site_dict = {}
    for line in molecule_lines:
        if line.startswith("#") or "(" not in line:
            continue
        match = re.match(r'(\w+)\((.*?)\)', line.strip())
        if not match:
            continue
        molecule, sites_block = match.groups()
        sites = [s.strip() for s in sites_block.split(",") if s.strip()]
        mol_site_dict[molecule] = sites
    return mol_site_dict


# process molecules
begin_index = None
end_index = None

for index, line in enumerate(lines):
    if line.lower().startswith("begin molecule types") or line.lower().startswith("begin molecules"):
            begin_index = index
    elif line.lower().startswith("end molecule types") or line.lower().startswith("end molecules"):
            end_index = index
            break
    
if begin_index is None and end_index is None: 
    print('No molecule types found in the file.')
    sys.exit()
    
molecule_lines = [lines[i].strip() for i in range(begin_index + 1, end_index)]
mol_site_dict = molecule_site_dict(molecule_lines)
converted_lines = []
for line in molecule_lines:
    if line.startswith('#'):
        continue  # Skip empty lines and comments
    converted_lines.append(bngl_to_railroad(line))


# process species
begin_species = None
end_species = None

for index, line in enumerate(lines):
    if line.lower().startswith("begin species") or line.lower().startswith("begin seed species"):
            begin_species = index
    elif line.lower().startswith("end species") or line.lower().startswith("end seed species"):
            end_species = index
            break


if begin_species is None and end_species is None:
    print('No species found in the file.')
    species_lines = []
else:
    species_lines = [lines[i].strip() for i in range(begin_species + 1, end_species)]

converted_species = []
for line in species_lines:
    if line.startswith('#') or not line:
        continue  
    parts = line.split()
    species = None
    for part in parts:
        if part.isdigit() or not part:
            continue
        if "(" in part and ")" in part:
            species = part
            if ":" in species:
                species = species.split(":")[1]
                break  

    if not species and ")" in line:
        end = line.index(")")
        species = line[:end+1]
    
    if species:
        converted_species.append(bngl_to_railroad(species))

# expand observables
from _expanded import expand_expr

# process observables
begin_obs = None
end_obs = None

for index, line in enumerate(lines):
    if line.lower().startswith("begin observables"):
            begin_obs = index
    elif line.lower().startswith("end observables"):
            end_obs = index
            break

if begin_obs is None and end_obs is None:
    print('No observables found in the file.')
    obs_lines = []
else:
    obs_lines = [lines[i].strip() for i in range(begin_obs + 1, end_obs)]

converted_obs = []
for line in obs_lines:
    if line.startswith('#') or not line:
        continue  
    parts = line.split()
    bngl_expr = " ".join(parts[2:])
    if ":" in bngl_expr:
        bngl_expr = bngl_expr.split(':')[1]
    display_string = bngl_expr
    expanded = expand_expr(bngl_expr, mol_site_dict)
    converted_obs.append(bngl_to_railroad(expanded, display_string))

# reaction rules
begin_reaction = None
end_reaction = None


for index, line in enumerate(lines):
   if line.lower().startswith("begin reaction"):
           begin_reaction = index
   elif line.lower().startswith("end reaction"):
           end_reaction = index
           break


if begin_reaction is None and end_reaction is None:
   print('No reaction rules found in the file.')
   reaction_lines = []
else:
    reaction_lines = [lines[i].strip() for i in range(begin_reaction + 1, end_reaction)]


converted_reaction = []
for line in reaction_lines:
    if line.startswith('#') or line.strip() == "":
       continue  # Skip empty lines and comments
    
    if ":" in line:
        line = line.split(":", 1)[1].strip()

   # Split into reactants and products
    if '<->' in line:
       arrow = '<->'
    elif '->' in line:
       arrow = '->'
    else:
       continue

    parts = line.split(arrow)
    reactants_str = parts[0].strip()
    products_str = parts[1].strip()

    stripped_r = []
    reactants = reactants_str.split(" + ")
    for part in reactants:
        part = part.strip()
        end_reactant_idx = part.rindex(")")
        part = part[:end_reactant_idx+1]
        if ":" in part:
            part = part.split(":")[1]
        stripped_r.append(part)
    reactants_str = " + ".join(stripped_r)

    stripped_p = []
    products = products_str.split(" + ")
    for part in products:
        part = part.strip()
        end_prod_idx = part.rindex(")")
        part = part[:end_prod_idx+1]
        if ":" in part:
            part = part.split(":")[1]
        stripped_p.append(part)
    products_str = " + ".join(stripped_p)

    display_string = f'{reactants_str} {arrow} {products_str}'

    expanded_reactants = expand_expr(reactants_str.replace(" + ", "."), mol_site_dict)
    expanded_products = expand_expr(products_str.replace(" + ", "."), mol_site_dict)

    # reaction rules
    from compare_reactions import *
    changes_dict = compare_reactions(expanded_reactants, expanded_products, arrow, mol_site_dict)

    reaction_diagram = bngl_to_railroad(expanded_reactants, display_string, changes_dict)

    converted_reaction.append(reaction_diagram)

# Write to .py file
with open(output_file, "w") as of:
    print('\nWriting to python file:', output_file)
    of.write('sys.stdout.write("<h1>Molecules</h1>\\n")\n\n')
    for diagram in converted_lines:
        of.write(f"\n{diagram}")
    
    if converted_species:
        of.write('sys.stdout.write("<h1>Species</h1>\\n")\n\n')
        for species in converted_species:
            of.write(f"\n{species}")
        
    if converted_obs:
        of.write('sys.stdout.write("<h1>Observables</h1>\\n")\n\n')
        for obs in converted_obs:
            of.write(f"\n{obs}")

    if converted_reaction:
        of.write('sys.stdout.write("<h1>Reactions</h1>\\n")\n\n')
        for reaction in converted_reaction:
            of.write(f"\n{reaction}")

print(f"\nBNGL to Python conversion complete. Output saved to {output_file}.")


import railroad2