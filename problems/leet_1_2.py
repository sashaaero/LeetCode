# https://leetcode.com/problems/two-sum/
# Runtime 6.19 ms

def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in dict:
            return dict[res], i
        dict[nums[i]] = i


arr = list(map(int, input().split()))
sumNum = int(input())

print(twoSum(arr, sumNum))
