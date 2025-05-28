import re
import sys

MoleculeColor = 'lightblue'
SiteColor = 'lightgreen'
StateColor = 'yellow'

# Different colors for different names
Molecule_Colors = {}
Site_Colors = {}
State_Colors = {}
color_name_dict = {}

Colors = [
    "red", "green", "yellow", "blue", "lightblue", 
    "skyblue", "orange", "pink", "lightgreen",
    "violet", "coral", "lightsalmon", "plum",
    "turquoise"
]


def get_color(name, color_name_dict, colors = Colors):
    if name not in color_name_dict:
        color_name_dict[name] = colors[len(color_name_dict) % len(colors)]
    return color_name_dict[name]
 

def bngl_to_railroad(bngl_string):
    # Step 1: Split molecule name and sites
    mol_match = re.match(r"(\w+)\((.*)\)", bngl_string.strip())
    if not mol_match:
        print("BNGL string format is invalid.")
    
    molecule_name, site_block = mol_match.groups()
    sites = [s.strip() for s in site_block.split(',')]

    diagram_code = [f'add("{bngl_string.strip()}",\n    Diagram(Terminal("{molecule_name}", box_color="{MoleculeColor}"),']

    # Step 2: Process each site
    for site in sites:
        if '~' in site:
            # Split into site name and states
            parts = site.split('~')
            site_name = parts[0]
            states = parts[1:]

            state_choices = ', '.join(f'NonTerminal("~{state}", box_color="{StateColor}")' for state in states)
            site_code = f'''    Choice(0, Comment("    "), Sequence(Terminal("{site_name}", box_color='{SiteColor}'), Choice(0, Comment("    "), {state_choices}))),'''
        else:
            site_code = f'''    Choice(0, Comment("    "), Terminal("{site}", box_color='{SiteColor}')),'''
        
        diagram_code.append(site_code)

    diagram_code.append("   )\n)\n")
    return "\n".join(diagram_code)


# take .bngl file as input
filepath = input('BNGL filepath: ')
file = filepath + '.bngl'
with open(file, 'r') as f:
    print('\nOpening file for reading:', file)
    lines = f.readlines()
lines = [line.strip() for line in lines]

output_file = filepath + '_output.py'


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
    sys.exit()
    
    
molecule_lines = [lines[i].strip() for i in range(begin_index + 1, end_index)]
converted_lines = []
for line in molecule_lines:
    if line.startswith('#'):
        continue  # Skip empty lines and comments
    converted_lines.append(bngl_to_railroad(line))

# Write to .py file
with open(output_file, "w") as of:
    print('\nWriting to python file:', output_file)
    for diagram in converted_lines:
        of.write(f"\n{diagram}")

print(f"\nBNGL to Python conversion complete. Output saved to {output_file}.")


import railroad