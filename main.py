# https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums):
    final_array = []

    n = int(len(nums)/2)
    
    first_arr = nums[:n]
    second_arr = nums[n:]

    for i in range(n):
        final_array.append(first_arr[i])
        final_array.append(second_arr[i])
    
    return final_array

print(shuffle([2,5,1,3,4,7]))
print(shuffle([1,2,3,4,4,3,2,1]))
print(shuffle([1,1,2,2]))

# ------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final_array = []

        n = int(len(nums)/2)
    
        first_arr = nums[:n]
        second_arr = nums[n:]

        for i in range(n):
            final_array.append(first_arr[i])
            final_array.append(second_arr[i])
    
        return final_array
