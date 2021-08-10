import sys

def decipherPassword(case):
    pwd_size = int(case[0])
    message = case[1]
    result = ""
    sub = ""
    freq_dict = {}

    for i in range( len(message) - pwd_size + 1):
        sub = message[i: i+pwd_size]

        if sub not in freq_dict:
            freq_dict[sub] = 1
        else:
            freq_dict[sub] += 1

    #print(freq_dict)

    max_value = max(freq_dict.values())

    for key, value in freq_dict.items():
        if(value == max_value):
            result = key
            break
    
    return result





cases = []

while True:
    try:
        line = input().strip()
        while line == "":
            line = input().strip()
        
        line = line.split()
        if len(line) == 2:
            pw_size = int(line[0])
            text = line[1]
            cases.append([pw_size, text])
        else:
            pw_size = int(line[0])
            text = input().strip()
            while text == "":
                text = input().strip()
            cases.append([pw_size, text])
    except(EOFError):
        break

for case in cases:
    print(decipherPassword(case))



