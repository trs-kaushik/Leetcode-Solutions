def countWords(wordLen, maxVowels):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    def countHelper(prefix, numVowels):
        if len(prefix) == wordLen:
            print(prefix)
            return 1 if numVowels <= maxVowels else 0
        else:
            count = 0
            for c in vowels:
                if numVowels < maxVowels:
                    count += countHelper(prefix + c, numVowels + 1)
                    
            for c in consonants:
                count += countHelper(prefix + c, 0)

            return count

    return countHelper('', 0)

print(countWords(2,1))


#With DP matrix
def countWords(wordLen, maxVowels,dp):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    def countHelper(prefix, numVowels,dp):
        
        if dp[len(prefix)][numVowels]!=-1:
            return dp[len(prefix)][numVowels]
            
        if len(prefix) == wordLen:
            return 1 if numVowels <= maxVowels else 0
        else:
            count = 0
            for c in vowels:
                if numVowels < maxVowels:
                    count += countHelper(prefix + c, numVowels + 1,dp)
                    
            for c in consonants:
                count += countHelper(prefix + c, 0,dp)

            dp[len(prefix)][numVowels] = count
            return dp[len(prefix)][numVowels]

    return countHelper('', 0,dp)

dp = [[-1 for i in range(1)] for j in range(3)]
print(countWords(2,0,dp))
