# compare the reactant and products, note the change

# define changes
state_change_up = "change from bottom state to top state"
state_change_down = "change from top state to bottom state"

bond_added_non_rev = "nradded"
bond_removed_non_rev = "nrbroken"
bond_added_rev = "radded"
bond_removed_rev = "rbroken"

def compare_reactions(expanded_reactants, expanded_products, arrow):
    stripped_changes = {}
    changes_dict = {}

    reactant_parts = expanded_reactants.split(".")
    product_parts = expanded_products.split(".")

    all_rsites = []
    for part in reactant_parts:
        rsites = part.split("(")[1].rstrip(")")
        rsites_parts = rsites.split(",")
        all_rsites+=rsites_parts
    
    all_psites = []
    for part in product_parts:
        psites = part.split("(")[1].rstrip(")")
        psites_parts = psites.split(",")
        all_psites+=psites_parts
    
    for i in range(len(all_rsites)):
        if all_rsites[i] != all_psites[i]:
            changes_dict[all_rsites[i]] = all_psites[i]
    
    for key,value in changes_dict.items():
        if "~" in key:
            rstate = "~"+key.split("~",-1)[-1]
            if "!" in rstate:
                rstate = rstate.split("!")[0]
            stripped_changes[rstate] = ""
        else:
            rbond = "!"+key.split("!")[-1]
            stripped_changes[rbond] = ""
        
        if "~" in value:
            pstate = "~"+value.split("~",-1)[-1]
            if "!" in pstate:
                pstate = pstate.split("!")[0]
            stripped_changes[rstate] = pstate
        else:
            pbond = "!"+value.split("!")[-1]
            stripped_changes[rbond] = pbond

        print(stripped_changes)
    

            
    


#test
compare_reactions("egfr(l!-,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?).egf(r!-)", 
                  "egfr(l!1,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?).egf(r!1)",
                  "<->" 
)

compare_reactions("egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?).egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?)", 
                  "egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?).egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?)",
                  "<->" 
)

compare_reactions("egfr(l!+,r!-,Y1068~Y!?,Y1148~Y~pY!?).egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?)", 
                  "egfr(l!+,r!3,Y1068~pY!?,Y1148~Y~pY!?).egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?)",
                  "<->" 
)

compare_reactions("egfr(l!?, r!+,Y1068~Y!-, Y1148~Y~pY!?)", 
                  "egfr(l!?, r!+,Y1068~pY!-, Y1148~Y~pY!?)", 
                  "->"
)

compare_reactions("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~Y!-)",
                  "egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~pY!-)",
                  "->" 
)

compare_reactions("egfr(l!?, r!+,Y1068~pY!-, Y1148~Y~pY!?)", 
                  "egfr(l!?, r!+,Y1068~Y!-, Y1148~Y~pY!?)",
                  "->" 
)

compare_reactions("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~pY!-)",
                  "egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~Y!-)", 
                  "->" 
)

compare_reactions("egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~Y!-)", 
                  "egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~pY!-)",
                  "->" 
)

compare_reactions("Shc(PTB!+,Y317~pY!-)", 
                  "Shc(PTB!+,Y317~Y!-)",
                  "->" 
)



    



# change in state - take the original molecule, and apply the multiple choice 

# up-arrow if change from bottom state to top state

# down-arrow if change from top state to bottom state



# change in bonds - take molecule with bond number (either reactant or product)

# if the arrow is --> and the bond is added, add nradded to product

# if the arrow is --> and the bond is removed, add nrbroken to reactant

# if the arrow is <--> and the bond is added, add radded to product

# if the arrow is <--> and the bond is removed, add rbroken to reactant