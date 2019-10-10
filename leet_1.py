# https://leetcode.com/problems/two-sum/
# Runtime 6.42 ms

def pairs(arr, arr_size, num):
    s = set()
    for i in range(0, arr_size):
        temp = num - arr[i]
        if (temp in s):
            print("Pair with given sum " + str(num) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i])


arr = list(map(int, input().split()))
sumNum = int(input())

pairs(arr, len(arr), sumNum)
