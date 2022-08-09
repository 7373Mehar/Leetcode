def maximumWealth(accounts):
    maxWealth = 0
    for i in range(len(accounts)):
        totalWealth = sum(accounts[i])
        maxWealth = max(maxWealth,totalWealth)
    return maxWealth

accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))
