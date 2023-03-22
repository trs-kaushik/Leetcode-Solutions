class Solution:
        def rob_recurse(self,ind, nums, dp):
                if dp[ind]!=None:
                        return dp[ind]
                if ind <0: return 0
                left = nums[ind] + self.rob_recurse(ind-2,nums, dp)
                right = 0 + self.rob_recurse(ind-1,nums, dp)
                dp[ind] = max(left,right)
                return dp[ind]

        def rob(self, nums: List[int]) -> int:
                dp = [None]*len(nums)
                dp[0] = nums[0]
                return self.rob_recurse(len(nums)-1, nums, dp)


#House Robber 2
class Solution:
        def rob(self, nums: List[int]) -> int:
                
                if(len(nums)==2):
                        return max(nums)
                dp = [[0 for i in range(2)] for i in range(len(nums))]
                dp[0][0] = 0
                dp[0][1] = nums[0]

                for i in range(1,len(nums)):
                        dp[i][1] = dp[i-1][0] + nums[i]
                        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                
                if(dp[len(nums)-1][1] - dp[len(nums)-2][0] > nums[0]):
                        return max(dp[len(nums)-1][1]-nums[0],dp[len(nums)-1][0])
                else:
                        return max(dp[len(nums)-2][1],dp[len(nums)-2][0])

        



