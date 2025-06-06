# test after unforking
# define changes
state_change_up = "change from bottom state to top state"
state_change_down = "change from top state to bottom state"

bond_added_non_rev = "nradded"
bond_removed_non_rev = "nrbroken"
bond_added_rev = "radded"
bond_removed_rev = "rbroken"

def compare_reactions(expanded_reactants, expanded_products, arrow, mol_site_dict):
    changes_dict = {}

    reactant_parts = expanded_reactants.split(".")
    product_parts = expanded_products.split(".")

    all_rsites = []
    for part in reactant_parts:
        rmol = part.split("(")[0]
        rsites = part.split("(")[1].rstrip(")")
        rsites_parts = rsites.split(",")
        for site in rsites_parts:
            all_rsites.append((rmol, site))
    
    all_psites = []
    for part in product_parts:
        pmol = part.split("(")[0]
        psites = part.split("(")[1].rstrip(")")
        psites_parts = psites.split(",")
        for site in psites_parts:
            all_psites.append((pmol, site))
    
    for i in range(len(all_rsites)):
        rmol,r_raw = all_rsites[i]
        pmol,p_raw = all_psites[i]

        if r_raw != p_raw:
            rstate = pstate = None
            rsite = psite = None
            rbond = pbond = None
            change = ""
            if "~" in r_raw:
                rstate = "~"+r_raw.rsplit("~",1)[-1]
                rsite = r_raw.split("~")[0]
                if "!" in rstate:
                    rstate = rstate.split("!")[0]
            else:
                rbond = "!"+r_raw.split("!")[-1]
                rsite = r_raw.split("!")[0]
            
            if "~" in p_raw:
                pstate = "~"+p_raw.rsplit("~",1)[-1]
                psite = p_raw.split("~")[0]
                if "!" in pstate:
                    pstate = pstate.split("!")[0]
            else:
                pbond = "!"+p_raw.split("!")[-1]
                psite = p_raw.split("!")[0]   

            if rstate != pstate:
                mole_sites = mol_site_dict[rmol]
                for site in mole_sites:
                    if site.startswith(rsite+"~"):
                        state_list = site.split("~")[1:]
                        if state_list.index(rstate.split("~")[1]) <  state_list.index(pstate.split("~")[1]):
                            change = state_change_down
                        elif state_list.index(rstate.split("~")[1]) >  state_list.index(pstate.split("~")[1]):
                            change = state_change_up


            elif rbond != pbond:
                if arrow == "->":
                    if rbond == "!-":
                        change = bond_added_non_rev
                    else:
                        change = bond_removed_non_rev
                else:
                    if rbond == "!-":
                        change = bond_added_rev
                    else:
                        change = bond_removed_rev

            changes_dict[f'{rmol}:{rsite}'] = {
                "molecule" : rmol,
                "site" : rsite,
                "reactant" : r_raw,
                "product" : p_raw,
                "change" : change
            }
    
    return changes_dict

# change in bonds - take molecule with bond number (either reactant or product)

# if the arrow is --> and the bond is added, add nradded to product

# if the arrow is --> and the bond is removed, add nrbroken to reactant

# if the arrow is <--> and the bond is added, add radded to product

# if the arrow is <--> and the bond is removed, add rbroken to reactant