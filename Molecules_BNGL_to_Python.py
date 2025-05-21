import re
import sys

sys.stdout = open('Molecules_BNGL_to_Python.txt', 'w')

def bngl_to_railroad(bngl_string):
    # Step 1: Split molecule name and sites
    mol_match = re.match(r"(\w+)\((.*)\)", bngl_string.strip())
    if not mol_match:
        raise ValueError("BNGL string format is invalid.")
    
    molecule_name, site_block = mol_match.groups()
    sites = [s.strip() for s in site_block.split(',')]

    diagram_code = [f'Diagram("{"{}(".format(molecule_name)}",']

    # Step 2: Process each site
    for site in sites:
        if '~' in site:
            # Split into site name and states
            parts = site.split('~')
            site_name = parts[0]
            states = parts[1:]
            state_choices = ', '.join(f'"~{state}"' for state in states)
            site_code = f'''    Choice(0, Comment("              "), Sequence("{site_name}", Choice(0, Comment("            "), {state_choices}))),'''
        else:
            site_code = f'''    Choice(0, Comment("                "), "{site}"),'''
        
        diagram_code.append(site_code)

    diagram_code.append('    ")"\n)')
    return "\n".join(diagram_code)


# test1
input_test1 = "EGFR(ecd,tmd,y1068~u~p,y1173~u~p)"
print(bngl_to_railroad(input_test1))

# test2
input_test2 = 'MAP3K(s, S~I~A)'
print(bngl_to_railroad(input_test2))

# test3
input_test3 = 'Grb2(sh2,sos)'
print(bngl_to_railroad(input_test3))

# test4
input_test4 = 'Shc(sh3,Y773~p~u)'
print(bngl_to_railroad(input_test4))

# test5
input_test5 = 'C(site,Y1~u~p,Y2~u~p,Y3~u~p)'
print(bngl_to_railroad(input_test5))

# test6
input_test6 = 'S(E~0~1,F~0~1,A~0~1,Y~U~P~2P~3P~4P~5P~6P~7P~8P~9P~10P~11P~12P~13P~14P~15P~16P~17P~18P~19P~20P)'
print(bngl_to_railroad(input_test6))

# test7
input_test7 = 'ErbB3(I_III,II,Y1054~O~P,Y1197~O~P,Y1222~O~P,Y1260~O~P,' \
                'Y1276~O~P,Y1289~O~P,Y1328~O~P,loc~M~En)'
print(bngl_to_railroad(input_test7))

# test8
input_test8 = 'Raf1(RBD,STkinase,S29~O~P,S43~O~P,S259~O~P,S289~O~P,S296~O~P,' \
                'S301~O~P,S338~O~P,Y341~O~P,S471~O~P,T491~O~P,S494~O~P,S642~O~P,loc~C)'
print(bngl_to_railroad(input_test8))