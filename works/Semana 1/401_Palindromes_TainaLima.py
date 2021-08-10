import sys

def isPalindrome(entry):
    return True if(entry == entry[::-1]) else False

def isMirrored(entry):
    reversedChar = { 'A':'A', 'E':'3', 'H': 'H', 'I': 'I','J': 'L','L': 'J','M': 'M','O': 'O','S': '2','T': 'T','U': 'U','V': 'V','W': 'W','X': 'X','Y': 'Y','Z': '5','1': '1','2': 'S', '3': 'E','5': 'Z','8': '8'}
    reversedEntry = []

    for char in entry:
        if char in reversedChar.keys():
            reversedEntry.append(reversedChar[char])
        else:
            reversedEntry.append('')

    return True if(entry == reversedEntry[::-1]) else False 

def isMirroredPalindrome(entry):
    entry_ = []
    entry_[:] = entry.strip("\n").strip("\t")

    isPalindrome_ = isPalindrome(entry_)
    isMirrored_ = isMirrored(entry_)

    if(isPalindrome_ and isMirrored_):
        return entry + " -- is a mirrored palindrome.\n"
    elif (isPalindrome_):
        return entry + " -- is a regular palindrome.\n"
    elif (isMirrored_):
        return entry + " -- is a mirrored string.\n"
    else:
        return entry + " -- is not a palindrome.\n"



if __name__ == "__main__":
    cases = []

    for line in sys.stdin:
        if line == '':
            break
        cases.append(line.strip())
    
    for case in cases:
        print(isMirroredPalindrome(case))
