
def getResult(shopPrices, availableMoney):
    for money in availableMoney:
        count = 0
        spent = 0
        for price in shopPrices:
            if(spent+price) <= money:
                spent += price
                count += 1
        print(count, money-spent)


noOfShops = input()
priceString = input()
priceList = priceString.split()
shopPrices = list(map(int, priceList))
noOfVisit = int(input())
savingAvailable = []
for i in range(noOfVisit):
    amount = input()
    savingAvailable.append(int(amount))

getResult(shopPrices, savingAvailable)
