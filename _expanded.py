def expand_expr(bngl_expr, mol_site_dict):
    chunks = bngl_expr.split('.')
    expanded_chunks = []
    for chunk in chunks:
        chunk = chunk.strip()

        if '(' in chunk and ')' in chunk:
            mol_end_idx = chunk.index('(')
            expr_end_idx = chunk.index(')')
            mol_name = chunk[:mol_end_idx]
            inside = chunk[mol_end_idx+1:expr_end_idx]

            given_sites = {}
            for s in inside.split(','):
                s = s.strip()
                s_base = s.split('~')[0].split('!')[0]
                given_sites[s_base] = s

            sites = mol_site_dict.get(mol_name, [])
            all_sites = []
            for site in sites:
                base = site.split('~')[0].split('!')[0]
                if base in given_sites:
                    s = given_sites[base]
                    if "!" not in s:
                        s += "!-"
                    all_sites.append(s)
                else:
                    site += "!?"
                    all_sites.append(site)

            updated_inside = ','.join(all_sites)
            expanded_chunks.append(f"{mol_name}({updated_inside})")
             
        elif chunk in mol_site_dict:
            inside = ",".join(f'{s}!?' for s in mol_site_dict[chunk])
            expanded_chunks.append(f"{chunk}({inside})")
        else:
            expanded_chunks.append(chunk)
    return ".".join(expanded_chunks)