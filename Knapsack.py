n = 3
wt = [3,4,5]
val = [30,40,40]
target = 8

def knapsack(ind, wt, val, target):
        if ind == 0:
                return val[ind]
        if dp[ind][target]!=-1:
                return dp[ind][target]
                
        pick = 1e-1      
        if wt[ind] <= target:
                pick = val[ind]+knapsack(ind-1, wt, val, target-wt[ind])
        
        n_pick = 0 + knapsack(ind-1, wt, val, target)
        
        dp[ind][target] = max(pick, n_pick)
        return dp[ind][target]

dp = [[-1 for i in range(target+1)] for j in range(n)]

for i in range(target):
        dp[0][i] = val[0]
        
for ind in range(1,n):
        for target in range(target):
                pick = 1e-1      
                if wt[ind] <= target:
                        pick = val[ind]+dp[ind-1][target-wt[ind]]
                
                n_pick = 0 + dp[ind-1][target]
                
                dp[ind][target] = max(pick, n_pick)
print(dp[n-1][target-1])
print(knapsack(n-1, wt, val, target))
