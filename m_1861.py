def rotateTheBox(self, box):
    for i in range(len(box)):
        stones = []
        for j in range(len(box[i])):
            if box[i][j] == '#':
                stones.append(j)
                
            if box[i][j] == '*':
                stones = []
                continue
            
            if box[i][j] == '.':
                self.moveStones(stones, box, i, j)
                
    return self.rotateBox(box)

def moveStones(self, stones, box, i, j):
    if len(stones) != 0:
        smallest = stones[0]
        box[i][j] = '#'
        box[i][smallest] = '.'
        stones.pop(0)
        stones.append(j)

def rotateBox(self, box):
    ans = []
    for i in range(len(box[0])):
        temp = []
        for j in range(len(box)):
            temp.append(box[len(box)-1 - j][i])
        ans.append(temp)
    
    return ans

# https://leetcode.com/problems/rotating-the-box/
# Time Complexity: O(n * m) where its n x m matrix 
# Space Complexity: O(m) from n x m matrix