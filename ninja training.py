training = [[1,2,5],[3,1,1],[3,3,3]]
def max_train(ind,train,last,dp):
        if dp[ind][last]!=-1:
                return dp[ind][last]
        if ind == 0:
                maxi = 0
                for i in range(0,3):
                        if i!=last:
                                maxi = max(maxi, train[ind][i])
                return maxi
                
        maxi = 0
        for i in range(3):
                if i != last:
                        maxi = max(maxi, train[ind][i] + max_train(ind-1,train, i,dp))
        dp[ind][i] = maxi
        return maxi
        
dp = [[-1 for i in range(4)] for j in range(3)]
print(max_train(len(training)-1, training, 3,dp))

dp[0][0] = max(training[0][1],training[0][2])
dp[0][1] = max(training[0][0],training[0][2])
dp[0][2] = max(training[0][0],training[0][1])
dp[0][3] = max(training[0][1],max(training[0][1],training[0][2]))

for day in range(1,3):
        for last in range(4):
                dp[day][last] = 0
                for i in range(3):
                        if i != last:
                                dp[day][last] = max(dp[day][last],training[day][i]+dp[day-1][i])
print(dp)
                
                
                                
                                
                        
