import itertools

def findChildBloodType(family):
    ABORELATION = {'AA': 'A', 'AB': 'AB', 'AO': 'A', 'BB': 'B', 'BO': 'B', 'OO': 'O'}
    RHFACTOR = { '+-': '+', '++': '+', '--' : '-'}

    parent1 = {'ABO': family[0][:len(family[0])-1], 'Rh': family[0][-1:]}
    parent2 = {'ABO': family[1][:len(family[1])-1], 'Rh': family[1][-1:]}
    child = {'ABO': [], 'Rh': []}
    #print(parent1)
    #print(parent2)

    possible_comb_p1 = {'ABO': [], 'Rh': []}
    possible_comb_p2 = {'ABO': [], 'Rh': []}

    for combinations, blood_type in ABORELATION.items():
        #print(combinations, blood_type)
        if(parent1['ABO'] == blood_type):
            possible_comb_p1['ABO'].append(combinations)
            #print(possible_comb_p1)
        if(parent2['ABO'] == blood_type):
            possible_comb_p2['ABO'].append(combinations)
            #print(possible_comb_p2)


    for rh_combinations, rh in RHFACTOR.items():
        if(parent1['Rh'] == rh):
            possible_comb_p1['Rh'].append(rh_combinations)
        if(parent2['Rh'] == rh):
            possible_comb_p2['Rh'].append(rh_combinations)
    
    #print(possible_comb_p1)
    #print(possible_comb_p2)

    for combination_p1 in possible_comb_p1['ABO']:
        comb_list_p1 = list(combination_p1)

        for combination_p2 in possible_comb_p2['ABO']:
            comb_list_p2 = list(combination_p2)

            for combination_ch in itertools.product(comb_list_p1, comb_list_p2):
                combination_ch_modified = list(combination_ch)
                combination_ch_modified.sort()
                combination_ch_modified = ''.join(combination_ch_modified)

                if (ABORELATION[combination_ch_modified] not in child['ABO']):
                    child['ABO'].append(ABORELATION[combination_ch_modified])

    for combination_p1 in possible_comb_p1['Rh']:
        comb_list_p1 = list(combination_p1)

        for combination_p2 in possible_comb_p2['Rh']:
            comb_list_p2 = list(combination_p2)

            for combination_ch in itertools.product(comb_list_p1, comb_list_p2):
                combination_ch_modified = list(combination_ch)
                combination_ch_modified.sort()
                combination_ch_modified = ''.join(combination_ch_modified)

                if (RHFACTOR[combination_ch_modified] not in child['Rh']):
                    child['Rh'].append(RHFACTOR[combination_ch_modified])
    
    result_string = []
    nOfFinaCombinations = 0
    #print(child)
    
    for final_combination_ch in itertools.product(child['ABO'], child['Rh']):
        
        blood_type_ch = ''.join(list(final_combination_ch))

        result_string = result_string + [blood_type_ch]

        nOfFinaCombinations += 1

    result_string.sort(reverse=True)
    result_string.sort(key=len, reverse=True)

    result_string = ', '.join(result_string)

    if(nOfFinaCombinations > 1):
        result_string = "{" + result_string + "}"

    return result_string

def findParentBloodType(family):
    ABORELATION = {'AA': 'A', 'AB': 'AB', 'AO': 'A', 'BB': 'B', 'BO': 'B', 'OO': 'O'}
    RHFACTOR = { '+-': '+', '++': '+', '--' : '-'}

    parent1 = {'ABO': [], 'Rh': []} if family[0] == "?" else {'ABO': family[0][:len(family[0])-1], 'Rh': family[0][-1:]}
    parent2 = {'ABO': [], 'Rh': []} if family[1] == "?" else {'ABO': family[1][:len(family[1])-1], 'Rh': family[1][-1:]}
    child = {'ABO': family[2][:len(family[2])-1], 'Rh': family[2][-1:]}

    possible_comb_p = {'ABO': [], 'Rh': []}
    possible_comb_ch = {'ABO': [], 'Rh': []}

    if(parent1['ABO']):
        parent = parent1
        missing_info_parent = parent2
    else:
        parent = parent2
        missing_info_parent = parent1

    for combinations, blood_type in ABORELATION.items():
        #print(combinations, blood_type)
        if(parent['ABO'] == blood_type):
            possible_comb_p['ABO'].append(combinations)
            #print(possible_comb_p1)
        if(child['ABO'] == blood_type):
            possible_comb_ch['ABO'].append(combinations)
            #print(possible_comb_p2)

    for rh_combinations, rh in RHFACTOR.items():
        if(parent['Rh'] == rh):
            possible_comb_p['Rh'].append(rh_combinations)
        if(child['Rh'] == rh):
            possible_comb_ch['Rh'].append(rh_combinations)

    #print(possible_comb_p)
    #print(possible_comb_ch)
    
    for abo_combinations in possible_comb_ch['ABO']:
        abo_alleles_list = list(abo_combinations)
        #print(abo_alleles_list)
        result = findMissingParentAlleleInfo(possible_comb_p, abo_alleles_list) 
        #print(parent_inherited_allele)
        #print(parent_missing_inherited_allele)

        for possible_parents_abo in result:
            parent_inherited_allele = possible_parents_abo[0]
            parent_missing_inherited_allele = possible_parents_abo[1]

            if(parent_inherited_allele != "-1" and parent_missing_inherited_allele != "-1"):
                for combi, blood_type in ABORELATION.items():
                    if(parent_missing_inherited_allele in combi) and (blood_type not in missing_info_parent['ABO']):
                        missing_info_parent['ABO'].append(blood_type)

    for rh_combinations in possible_comb_ch['Rh']:
        rh_list = list(rh_combinations)

        result2 = findMissingParentRhInfo(possible_comb_p, rh_list) 

        for possible_parents_rh in result2:
            parent_inherited_rh = possible_parents_rh[0]
            parent_missing_inherited_rh = possible_parents_rh[1]

            if(parent_inherited_rh != "-1" and parent_missing_inherited_rh != "-1"):
                for combi, rh in RHFACTOR.items():
                    if(parent_missing_inherited_rh in combi) and (rh not in missing_info_parent['Rh']):
                        missing_info_parent['Rh'].append(rh)

    if (missing_info_parent['ABO'] and missing_info_parent['Rh']):
        result_string = []
        nOfFinaCombinations = 0
        #print(child)
        
        for final_combination_ch in itertools.product(missing_info_parent['ABO'], missing_info_parent['Rh']):
            
            blood_type_ch = ''.join(list(final_combination_ch))

            result_string = result_string + [blood_type_ch]

            nOfFinaCombinations += 1

        result_string.sort(reverse=True)
        result_string.sort(key=len, reverse=True)
        
        result_string = ', '.join(result_string)

        if(nOfFinaCombinations > 1):
            result_string = "{" + result_string + "}"
    else:
        result_string = "IMPOSSIBLE"

    return result_string

def findMissingParentAlleleInfo(parent, child_alleles):
    result = []
    if any(child_alleles[0] in abo_combination for abo_combination in parent['ABO']):
        result.append([child_alleles[0], child_alleles[1]])
    if any(child_alleles[1] in abo_combination for abo_combination in parent['ABO']):
        result.append([child_alleles[1], child_alleles[0]])
    else:
        result.append(["-1", "-1"])

    return result

def findMissingParentRhInfo(parent, rh_list):
    result = []
    if any(rh_list[0] in rh_combination for rh_combination in parent['Rh']):
        result.append([rh_list[0], rh_list[1]])
    if any(rh_list[1] in rh_combination for rh_combination in parent['Rh']):
        result.append([rh_list[1], rh_list[0]])
    else:
        result.append(["-1", "-1"])
    return result

def consanguineCalculations(case):

    family = case.strip().split()

    if(family[2] == "?"):
        family[2] = findChildBloodType(family)
    else:
        result = findParentBloodType(family)

        if(family[0] == "?"):
            family[0] = result
        else: 
            family[1] = result

    return family[0] + " " + family[1] + " " + family[2]

if __name__ == "__main__":
    cases = []

    #f = open("output.txt", 'w')

    case = str(input())
    while (case.strip() != 'E N D'):
        cases.append(case)
        case = str(input())

    for i in range(len(cases)):
        result = consanguineCalculations(cases[i])
        print("Case " + str(i+1) + ": " + result)


    #f.close()