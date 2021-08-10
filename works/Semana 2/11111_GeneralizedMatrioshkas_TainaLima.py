import sys

def isGeneralizedMatrioshka(case):
    if(case):
        entry = case.split()
        stack_matrioshka = []
        stack_inner_sum_matrioshka = [0]
        isMatrioshka = True

        stack_matrioshka.append(int(entry[0]))
        for m in entry[1:]:
            matrioshka = int(m)
            #print(m)
            #print(stack_matrioshka)
            #print(stack_inner_sum_matrioshka)
            if(matrioshka < 0):
                stack_inner_sum_matrioshka[-1] += -matrioshka
                stack_matrioshka.append(matrioshka)
                stack_inner_sum_matrioshka.append(0)

            else:
                if(stack_matrioshka[-1] == -matrioshka):
                    if(stack_inner_sum_matrioshka[-1] >= matrioshka):
                        isMatrioshka = False
                        break
                    stack_matrioshka.pop()
                    stack_inner_sum_matrioshka.pop()
                else:
                    isMatrioshka = False
                    break

        if(stack_matrioshka or stack_inner_sum_matrioshka):
            isMatrioshka = False
    else:
        return False

    return isMatrioshka


if __name__ == '__main__':

    cases = []

    for line in sys.stdin:                                
        if line == '':
            break
        cases.append(line.strip())

    for case in cases:
        #print(case)
        print(":-) Matrioshka!" if isGeneralizedMatrioshka(case) else ":-( Try again.")
