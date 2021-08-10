def readTestCases():
    cases = []
    
    nOfTestCase = int(input())

    for x in range(nOfTestCase):
        cases.append(str(input()))

    return nOfTestCase, cases

def convertStrToCharList(string):
    list1=[]
    list1[:0]=string
    return list(filter(lambda a: (a == "(") or (a == ")") or (a == "[") or (a == "]"), list1))

def isParenthesesBalanced(string):
    if string == "":
        return True
    else:
        str_stack = convertStrToCharList(string)

        aux_stack = []

        while len(str_stack) != 0:
            aux_stack.append(str_stack.pop())

            aux_stack_top = len(aux_stack) - 1

            str_from_top = aux_stack[aux_stack_top] + aux_stack[aux_stack_top-1]

            if(str_from_top == "()") or (str_from_top == "[]"):
                aux_stack = aux_stack[:aux_stack_top-1]
        
        if(len(aux_stack) == 0):
            return True
        else:
            return False

if __name__ == "__main__":
    nOfStrings, strings = readTestCases()

    for string in strings: 
        print("Yes" if isParenthesesBalanced(string) else "No")

