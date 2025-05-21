import sys

sys.stdout = open('Species_BNGL_to_Python.txt', 'w')

import re

def bngl_species_to_railroad(bngl_species):
    # Fixed comment spacings
    OUTER_COMMENT = 'Comment("                                ")'
    INNER_COMMENT = 'Comment("                ")'
    INNERMOST_COMMENT = 'Comment("    ")'

    diagram_code = ['Diagram(']

    # Split molecules by '.'
    molecules = bngl_species.strip().split('.')
    
    for idx, molecule in enumerate(molecules):
        mol_match = re.match(r"(\w+)\((.*)\)", molecule)
        if not mol_match:
            raise ValueError(f"Invalid molecule format: {molecule}")
        
        mol_name, site_block = mol_match.groups()
        sites = [s.strip() for s in site_block.split(',') if s.strip()]

        # Molecule opening
        diagram_code.append(f"   '{mol_name}(',")
        
        # Handle each site
        for site in sites:
            site_match = re.match(r"(\w+)(?:~(\w+))?(?:(!\d+))?", site)
            if not site_match:
                raise ValueError(f"Invalid site format: {site}")
            site_name, state, bond = site_match.groups()

            # CASE 1: site with no state and no bond → flat choice
            if not state and not bond:
                site_code = f"    Choice(0, {OUTER_COMMENT}, '{site_name}'),"
            else:
                # build inner content
                if state and bond:
                    inner = f"Sequence('~{state}', Choice(0, {INNERMOST_COMMENT}, '{bond}'))"
                elif state:
                    inner = f"'~{state}'"
                elif bond:
                    inner = f"'{bond}'"

                site_code = (
                    f"    Choice(0, {OUTER_COMMENT}, \n"
                    f"           Sequence('{site_name}',\n"
                    f"                    Choice(0, {INNER_COMMENT}, {inner})\n"
                    f"           )),"
                )
            diagram_code.append(site_code)

        # Close molecule
        diagram_code.append("    ')',")

        # Dot separator between molecules
        if idx < len(molecules) - 1:
            diagram_code.append("    '.',")

    # Close Diagram
    diagram_code.append(")")
    return "\n".join(diagram_code)



input_test1 = "MAP2K(s,R1~Y,R2~Y)"
print(bngl_species_to_railroad(input_test1))

input_test2 = "M1R(L,S228~u,S273~u,Arr,GRK,PP1,CK2)"
print(bngl_species_to_railroad(input_test2))

input_test3 = "Oxo(R!1).M1R(L!1,S228~u,S273~u,Arr,GRK,PP1,CK2)"
print(bngl_species_to_railroad(input_test3))

input_test4 = "Oxo(R!1).M1R(L!1,S228~p,S273~p,Arr!2,GRK,PP1,CK2).Arrestin(RLP!2,MEK!3,PP2A).MEK(Arr!3,ERK)"
print(bngl_species_to_railroad(input_test4))

input_test5 = "Tie2(tie1bs,loc~sol,veptpbs,pY~dp,ang1bs,ang2bs)"
print(bngl_species_to_railroad(input_test5))

input_test6 = "NFkB(Ikba!0,loc~cyt).IkBa(Nfkb!0,loc~cyt,Ser32_Ser36~0)"
print(bngl_species_to_railroad(input_test6))