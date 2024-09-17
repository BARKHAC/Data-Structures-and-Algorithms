# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]: 
#         myAns=[]
#         nums_len=len(nums)
#         for i in range(0,nums_len):
#             for j in range(i+1,nums_len):
#                 if(nums[i] + nums[j] == target and i>j):
#                    myAns.append(j)
#                    myAns.append(i)
#                    return myAns
#                 elif(nums[i] + nums[j] == target):
#                    myAns.append(i)
#                    myAns.append(j)
#                    print(myAns)
#                    return myAns

#Brute Force using arrays and two for loops O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:      #HashMap O(n)
        prevMap = {} 

        for i,n in enumerate(nums):
            diff = target -n #target - curr num
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n] = i
            

                


if __name__ == "__main__":
    solution = Solution()

    nums = [2,7,11,15]
    target =9

    result = solution.twoSum(nums,target)
    print (result)