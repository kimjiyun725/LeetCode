# version 1, exceeded time
def numPairsDivisibleBy60(self, time) -> int:
    d = {idx: val for (idx, val) in enumerate(time)}
    pairs = 0
    for i in range(len(time)):
        del d[i]
        for j in d:
            if i >= j:
                continue
            if (time[i] + d[j]) % 60 != 0:
                continue
            pairs += 1
    
    return pairs

# version 2, 2 dictionaries (time exceeded)
def numPairsDivisibleBy60(self, time) -> int:
    d = {}
    s = {}
    for (idx,val) in enumerate(time):
        d[idx] = val
        if val not in s:
            s[val] = {idx}
        else:
            s[val].add(idx)
            
    pairs = 0
    while d != {}:
        f = next(iter(d))
        print(f)
        for row in s:
            s[d[f]].discard(f)
            if (d[f] + row) % 60 == 0:
                pairs += len(s[row])
        del d[f]
                
    return pairs

# version 3, refined version of v2 (time exceeded)
def numPairsDivisibleBy60(self, time) -> int:
    s = {}
    for (idx,val) in enumerate(time):
        if val not in s:
            s[val] = {idx}
        else:
            s[val].add(idx)
    pairs = 0
    for i in range(len(time)):
        for row in s:
            s[time[i]].discard(i)
            if (time[i] + row) % 60 == 0:
                pairs += len(s[row])
        
    return pairs

# version 4, sometimes passes everything, sometimes exceeding time limit
def numPairsDivisibleBy60(self, time) -> int:
    d = {}
    pairs = 0
    for j in range(len(time)):
        for i in d:
            if (i + time[j]) % 60 == 0:
                pairs += d[i]['occurs']
                
        if time[j] not in d:
            d[time[j]] = {'occurs': 1}
        else:
            d[time[j]]['occurs'] += 1
                
    return pairs        

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Time Complexity: O(n^2) because for loop is length of list "time" 
# and the nested for loop is length of dictionary "d" which is length of list "time".
# Space Complexity: O(n) because it will create n'th keys where n = length of list "time"

