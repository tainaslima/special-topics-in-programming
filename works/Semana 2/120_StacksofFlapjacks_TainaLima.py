import sys

def flip(flip_list):

    stop = int(len(flip_list)/2)

    for i in range(stop):
        aux = flip_list[i]

        flip_list[i] = flip_list[len(flip_list)-1-i]

        flip_list[len(flip_list)-1-i] = aux

    return flip_list

def orderPancakesStack(case):
    stack = [ int(pancake) for pancake in case ]
    result = ""

    sorted_stack = stack.copy()
    sorted_stack.sort()

    if(stack == sorted_stack):
        return "0"

    else:
        i = len(stack) - 1
        while (i > 0):
            if (stack == sorted_stack):
                break 

            top = 0
            base = len(stack)-1 

            larger_pancake = stack.index(sorted_stack[i])

            if(larger_pancake != base):
                if(larger_pancake != top):
                    flip_list = stack[:larger_pancake+1]
                    rest_list = stack[larger_pancake+1:]

                    flip_list = flip(flip_list)

                    result = result + str(len(stack) - larger_pancake) + " "

                    stack = flip_list + rest_list

                stack[:i+1] = flip(stack[:i+1])

                result = result + str(len(stack) - i) + " "
            
            i -= 1

        return result + "0"



if __name__ == "__main__":
    cases = []

    for line in sys.stdin:
        if line == '':
            break
        cases.append(line.strip())

    for case in cases:
        print(case)
        print(orderPancakesStack(case.split()))