def getSmallestCaps(caps: int):
    totalCaps = caps
    rahulCaps = 0
    nehaCaps = 0
    k = 1
    while(True):
        print('K:', k)
        while(totalCaps > k):
            rahulCaps += k
            totalCaps -= k

            # print(rahulCaps)
            # print(totalCaps)
            nehaCaps += (totalCaps//10)
            totalCaps -= (totalCaps//10)
            # print(nehaCaps)
            # print(totalCaps)
            # print('RAHUL CAPS', rahulCaps)
            # print('NEHA CAPS', nehaCaps)
            # print('REMAINING CAPS', totalCaps)
        rahulCaps += totalCaps

        if(rahulCaps > nehaCaps):
            print(k)
            break
        else:
            totalCaps = caps
            nehaCaps = 0
            rahulCaps = 0
            k += 1


getSmallestCaps(68)
