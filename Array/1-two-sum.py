# Given an array of integers, return indices of the two
# numbers such that they add up to a specific target

def twoSum(arr, target):
    for i in range(len(arr)):
        if arr[i] + arr[i+1] == target:
            return [i,i+1]

print(twoSum([2, 7, 11, 15], 9))