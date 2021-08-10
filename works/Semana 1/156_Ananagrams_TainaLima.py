def findAnanagrams(domainDict):
    ananagrams = domainDict.copy()

    for x in range(len(domainDict)):
        base = []
        base[:] = domainDict[x].lower()
        base.sort()

        for y in range(x+1, len(domainDict)):
            compared_word = []
            compared_word[:] = domainDict[y].lower()
            compared_word.sort()

            if (base == compared_word):
                if (domainDict[x] in ananagrams):
                    ananagrams.remove(domainDict[x])
                if (domainDict[y] in ananagrams):
                    ananagrams.remove(domainDict[y])
                break
    
    ananagrams.sort()
    return ananagrams


if __name__ == "__main__":
    domainDict = []

    #f = open("output.txt", 'w')

    words = str(input())
    while (words.strip() != '#'):
        domainDict = domainDict + words.strip().split()
        words = str(input())
        
    ananagrams = findAnanagrams(domainDict)

    for ananagram in ananagrams:
        print(ananagram)


    #f.close()