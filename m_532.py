def findPairs(self, nums: List[int], k: int) -> int:
    d = {val: 0 for (idx, val) in enumerate(set(nums))}
    
    for num in nums:
        if num in d.keys():
            d[num] += 1
    
    pairs = {}
    nums.sort()
    for num in nums:
        if num not in pairs.keys():
            if num + k in d.keys():
                if num+k == num:
                    if d[num] > 1:
                        pairs[num] = (num, num+k)
                        d[num] -= 1
                        d[num+k] -= 1
                else:
                    pairs[num] = (num, num+k)
                    d[num] -= 1
                    d[num+k] -= 1   
    
    return len(pairs.keys())

# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Time Complexity: O(nlogn). O(nlogn) because of line 9 which uses the sort() function.
# the sort() function uses the Timsort algorithm.
# Space Complexity: O(n + n/2) aka O(n). O(n) because line 2 will create a dictonary with
# n'th keys (a little less since there are no dupes within its conditions).