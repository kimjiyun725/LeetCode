def pivotIndex(self, nums: List[int]) -> int:
    l_sum = 0
    r_sum = 0
    for i in range(1, len(nums)):
        r_sum += nums[i]
    
    if l_sum == r_sum:
        return 0
    
    for i in range(1, len(nums)):
        l_sum += nums[i-1]
        r_sum -= nums[i]
        if l_sum == r_sum:
            return i
                
    return -1
            
# Time Complexity: O(n+n) aka O(n). O(n) where n = length of list "nums"
# Space Complexity: O(n+n) aka O(n). O(n) where n = length of list "nums". 
# There are two variables, "l_sum" and "r_sum", that are updating inside a for loop.