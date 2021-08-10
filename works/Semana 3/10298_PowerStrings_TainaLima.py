import sys

def exponentialStr(word):
    if(word):
        max_subword_repetitions = 1
        max_subword = ""
        word_size = len(word)
        i_found_a = False
    
        for subword_size in range(1, word_size):
            #print(subword_size)
            if(word_size % subword_size == 0):

                for pointer in range(0, word_size-subword_size, subword_size):
                    subword1 = word[pointer:pointer+subword_size]
                    subword2 = word[pointer+subword_size:pointer+subword_size+subword_size]

                    #print("sub1", subword1)
                    #print("sub2", subword2)

                    if(subword1 != subword2):
                        i_found_a = False
                        break
                    i_found_a = True
                    
                    
                if(i_found_a):
                    max_subword = subword1
                    break
        
        max_subword_repetitions = 1 if len(max_subword) == 0 else word_size // len(max_subword)

        return max_subword, max_subword_repetitions
    else:
        return "", 0

cases = []
for line in sys.stdin:
    if line.strip() == ".":
        break
    cases.append(line.strip())

for case in cases:
    a, n = exponentialStr(case)
    print(n)