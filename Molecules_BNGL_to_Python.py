import re

MoleculeColor = 'lightgreen'
SiteColor = 'lightblue'
StateColor = 'khaki'

def bngl_to_railroad(bngl_string):
    mol_chunks = bngl_string.split('.')
    diagrams = [f'add("{bngl_string.strip()}",', "    Diagram("]

    for idx, chunk in enumerate(mol_chunks):
        mol_match = re.match(r"(\w+)\((.*)\)", chunk.strip())
        if not mol_match:
            print("BNGL string format is invalid.")
            continue
        
        molecule_name, site_block = mol_match.groups()
        sites = [s.strip() for s in site_block.split(',')]

        diagrams.append(f'        Terminal("{molecule_name}", box_color="{MoleculeColor}"),')

        # Step 2: Process each site
        for site in sites:
            bond_arg = ""
            bond_num_arg = ""
            bond_num = None

            site_name = site
            states = []
                 
            
            if '~' in site:
                # Split into site name and states
                parts = site.split('~')
                site_name = parts[0]
                states = parts[1:]

                fin_states = []
                for state in states:
                    bond_arg = ""
                    bond_num_arg = ""
                    if "!" in state:
                        state_split = state.split("!")
                        state_name = state_split[0]
                        bond_num = state_split[1]

                        if bond_num == "?":
                            bond_arg = ', bottom_bind=True, bottom_bind_color="gray"'
                            bond_num_arg = f', bond_num="{bond_num}"'
                        elif bond_num == "+":
                            bond_arg = ', bottom_bind=True'
                            bond_num_arg = f', bond_num="{bond_num}"'
                        elif bond_num.isdigit():
                            bond_arg = ', bottom_bind=True'
                            bond_num_arg = f', bond_num="{bond_num}"'
                        state = state_name
                    fin_states.append(f'NonTerminal("{state}", box_color="{StateColor}"{bond_arg}{bond_num_arg})')

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
                site_code = f'''    Choice(0, Comment("    "), Terminal("{site_name}", box_color='{SiteColor}'{bond_arg}{bond_num_arg})),'''
            
            diagrams.append(site_code)
        if idx < len(mol_chunks)-1:
            diagrams.append("        EndWhiteSpace(),")

    diagrams.append("    )\n)")
    return "\n".join(diagrams) + "\n"


# take .bngl file as input
filepath = input('BNGL filepath: ')
file = filepath + '.bngl'
with open(file, 'r') as f:
    print('\nOpening file for reading:', file)
    lines = f.readlines()
lines = [line.strip() for line in lines]

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
    if line.lower().startswith("begin molecule types"):
            begin_index = index
    elif line.lower().startswith("end molecule types"):
            end_index = index
            break
    
if begin_index is None and end_index is None: 
    print('No molecule types found in the file.')
    
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
else:
    obs_lines = [lines[i].strip() for i in range(begin_obs + 1, end_obs)]

converted_obs = []
for line in obs_lines:
    if line.startswith('#') or not line:
        continue  
    parts = line.split()
    bngl_expr = " ".join(parts[2:])
    expanded = expand_expr(bngl_expr, mol_site_dict)
    converted_obs.append(bngl_to_railroad(expanded))


# Write to .py file
with open(output_file, "w") as of:
    print('\nWriting to python file:', output_file)
    of.write('sys.stdout.write("<h1>Molecules</h1>\\n")\n\n')
    for diagram in converted_lines:
        of.write(f"\n{diagram}")
    
    of.write('sys.stdout.write("<h1>Species</h1>\\n")\n\n')
    for species in converted_species:
        of.write(f"\n{species}")
    
    of.write('sys.stdout.write("<h1>Observables</h1>\\n")\n\n')
    for obs in converted_obs:
        of.write(f"\n{obs}")

print(f"\nBNGL to Python conversion complete. Output saved to {output_file}.")


import railroad2