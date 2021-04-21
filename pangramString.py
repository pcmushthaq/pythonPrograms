# A pangram is a sentence where every letter of the
# English alphabet appears at least once.

# Given a string sentence containing only lowercase
#  English letters, return true if sentence is a pangram,
#  or false otherwise.

# Simple Solution
# return len(set(s)) == 26

def checkIfPangram(self, sentence: str) -> bool:
    uniqueCount = 0
    hashMap = {}
    for letter in sentence:
        if letter in hashMap:
            continue
        else:
            hashMap[letter] = True
            uniqueCount += 1
    if uniqueCount == 26:
        return True
    else:
        return False

# "thequickbrownfoxjumpsoverthelazydog"
# "leetcode"
