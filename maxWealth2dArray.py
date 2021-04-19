# You are given an m x n integer grid accounts
# where accounts[i][j] is the amount of money
# the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return
# the wealth that the richest customer has.

# A customer's wealth is the amount of money
# they have in all their bank accounts.
# The richest customer is the customer that has
# the maximum wealth.

def maxWealth(array):
    return max(map(sum, array))


accounts = [[1, 2, 3], [3, 2, 1]]
print(maxWealth(accounts))
