def getDuration(text):
    time = 0
    first = abs(
        ord('A')-ord(text[0].upper()))
    reverseDirectionCount = (
        26-first if first > 13 else first)
    time += (first if first <
             reverseDirectionCount else reverseDirectionCount)

    for i in range(len(text)-1):
        forwardDirectionCount = abs(
            ord(text[i+1].upper())-ord(text[i].upper()))
        reverseDirectionCount = (
            26-forwardDirectionCount if forwardDirectionCount > 13 else forwardDirectionCount)
        time += (forwardDirectionCount if forwardDirectionCount <
                 reverseDirectionCount else reverseDirectionCount)
        print(time)
    return time


print(getDuration('AZGB'))
