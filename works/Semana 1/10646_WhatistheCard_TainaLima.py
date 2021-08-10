def readTestCases():
    cases = []
    
    nOfTestCase = int(input())

    for x in range(nOfTestCase):
        cases.append(str(input()))

    return nOfTestCase, cases

def cardValue(card):
    return int(card[0]) if card[0].isdigit() else 10

if __name__ == "__main__":
    nOfTestCase, cases = readTestCases()

    for case_number in range(nOfTestCase):
        board_stack = cases[case_number].strip().split()

        hand_stack = board_stack[-25:]

        remaining_stack = board_stack[:27]
   
        y = 0

        for i in range(3):
            top_stack = remaining_stack.pop()
			
            x = cardValue(top_stack)

            y += x

            remaining_stack = remaining_stack[:len(remaining_stack) - (10-x)]
            
        
        board_stack_new = remaining_stack + hand_stack

        print("Case " + str(case_number+1) + ": " + board_stack_new[y-1])
        