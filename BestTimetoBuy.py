from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy when low sell when high
        l,r = 0,1
        profit=0
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices [l]
                maxP = max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP



if __name__ == "__main__":
    
  solution = Solution()
  result = solution.maxProfit([1,2])
  print(result)