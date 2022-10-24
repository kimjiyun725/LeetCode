def breakPalindrome(self, palindrome: str) -> str:
    if len(palindrome) == 1:
        return ""

    smallest_idx = -1
    for i in range(len(palindrome) // 2):
        if 'a' < palindrome[i] <= 'z':
            smallest_idx = i
            break
            
    if smallest_idx == -1:
        return ''.join([palindrome[:-1], 'b']) 
    return ''.join([palindrome[:smallest_idx], 'a', palindrome[smallest_idx+1:]])

# https://leetcode.com/problems/break-a-palindrome/
# Time Complextiy: O(n) where 'palindrome' is length of n and all for-loops iterates
# half of its length
# Space Complexity: O(n) because dictionary size is n // 2 where 
# n == length of 'palindrome'

