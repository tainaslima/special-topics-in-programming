import math, string

UPPERCASE_LETTERS = set(string.ascii_uppercase)

def findFiboIndex(n) :
    fibo = 2.078087 * math.log(n) + 1.672276

    return round(fibo)-1

def decipherCode(case):
    if(case):
        n_of_fibo = case[0]
        fibonacci_numbers = case[1]
        text = []
        text[:] = case[2]
        result = [""]*2*n_of_fibo
        fibos_used = [0]*n_of_fibo

        text_ = []
        for i in range(len(text)):
            if(text[i] in UPPERCASE_LETTERS):
                text_.append(text[i])

        #print(text_)
        #print(result)
        i = 0
        for fibo in fibonacci_numbers:
            fibo_index = findFiboIndex(int(fibo))
            #print(fibo_index)
            diff_ = fibo_index - len(result)
            if(diff_ > 0 ):
                result.extend([""] * diff_)
            result[fibo_index - 1] = text_[i]

            diff = fibo_index - len(fibos_used)
            if(diff > 0):
                fibos_used.extend([0] * diff)
            fibos_used[fibo_index - 1] = 1

            i += 1
        
        if(0 in fibos_used):
            for idx, word in enumerate(fibos_used):
                if word == 0:
                    result[idx] = " "

        return "".join(result)
    else:
        return ""

cases = []

number_of_cases = int(input())

i = 0
while(i < number_of_cases):
    n_of_fibo = int(input())
    fibonacci_numbers = input().strip().split()
    text = input().strip()

    cases.append([n_of_fibo, fibonacci_numbers, text])
    i += 1

for case in cases: 
    #print(case)
    print(decipherCode(case))