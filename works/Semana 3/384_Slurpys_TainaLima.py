import sys

INDEX = 0 


def isSlump(case):
    global INDEX
    if(case[INDEX] != 'D'):
        if(case[INDEX] != 'E'):
            return False
    INDEX += 1

    if(case[INDEX] != 'F'):
        return False
    INDEX += 1

    while(INDEX < len(case) and (case[INDEX] == 'F')) :
        INDEX += 1
    
    if(INDEX >= len(case)):
        return False

    if(case[INDEX] == 'G'):
        INDEX += 1
        return True
    else:
        return isSlump(case)


def isSlimp(case):
    global INDEX
    if(case[INDEX] != 'A'):
        return False
    INDEX += 1

    if(case[INDEX] == 'H'):
        INDEX += 1
        return True
    else:
        if(case[INDEX] == 'B'):
            INDEX += 1

            is_s = isSlimp(case) and (INDEX < len(case)) and (case[INDEX] == 'C')
            INDEX += 1
            return is_s
        
        is_s = isSlump(case) and (INDEX < len(case)) and (case[INDEX] == 'C')
        INDEX += 1
        return is_s

def isSlurpy(case):
    is_slurpy = isSlimp(case) and isSlump(case) and INDEX == len(case)

    return "YES" if is_slurpy else "NO"






cases = []

N = int(input())

i = 0
while(i < N):
    case = input().strip()

    if(case != ''):
        cases.append(case)
        i += 1

print("SLURPYS OUTPUT")

for case in cases: 
    INDEX = 0
    #print(case)
    print(isSlurpy(case))

print("END OF OUTPUT")