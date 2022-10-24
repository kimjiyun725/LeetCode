def breakPalindrome(self, palindrome: str) -> str:
    if len(palindrome) == 1:
        return ""

    length = len(palindrome) // 2
    char_vals = {i: ord(palindrome[i]) for i in range(length)}
    smallest_idx = -1
    for i in range(length):
        if ord('a') < char_vals[i] < ord('z')+1:
            smallest_idx = i
            break
            
    if smallest_idx == -1:
        return ''.join([palindrome[0:len(palindrome)-1], 'b'])
    
    return ''.join([palindrome[:smallest_idx], 'a', palindrome[smallest_idx+1:]])


# https://leetcode.com/problems/break-a-palindrome/
# Time Complextiy: O(n) 'palindrome' is length of n and all for-loops iterates
# half of its length
# Space Complexity: O(n) because dictionary size is n // 2 where 
# length of 'palindrome'

