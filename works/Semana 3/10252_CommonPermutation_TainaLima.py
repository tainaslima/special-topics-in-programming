import sys

def findX(case):
    if(len(case) == 2):
        a = case[0].strip()
        b = case[1].strip()

        letters_counter_a = {}

        for letter in a:
            if letter in letters_counter_a:
                letters_counter_a[letter] += 1
            else:
                letters_counter_a[letter] = 1

        intersection = []

        for letter in b:
            if letter in letters_counter_a:
                intersection.append(letter)
                letters_counter_a[letter] -= 1

                if letters_counter_a[letter] == 0:
                    del letters_counter_a[letter]

        intersection.sort()

        return "".join(intersection)
    else:
        return ""



if __name__ == '__main__':
    cases = []

    i = 0
    for line in sys.stdin:
        if line == '':
            break
        if(i == 0):
            case = [line.strip()]
            i = 1
        else:
            case.append(line.strip())
            cases.append(case)
            i = 0

    for case in cases:
        print(findX(case))