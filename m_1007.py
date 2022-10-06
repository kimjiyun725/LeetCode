def minDominoRotations(tops, bottoms) -> int:
    
    #A domino's number can only be between 1 to 6
    d = {num:{'top':0, 'bot': 0, 'total': 0} for num in range(1,7)}
    #Update the occurences of each value
    for i in range(len(tops)):
        if tops[i] != bottoms[i]:
            d[tops[i]]['top'] += 1
            d[tops[i]]['total'] += 1
            d[bottoms[i]]['bot'] += 1
            d[bottoms[i]]['total'] += 1
        else:
            #If top and bottom are the same, only increment the total
            d[tops[i]]['total'] += 1
    
    #Find which number showed up the most
    most = 0
    for key in d:
        if most == 0:
            most = key
            continue
            
        if d[most]['total'] < d[key]['total']:
            most = key
    
        #If there is a number with the same amount of occurence,
        #check which number has the most amount on their rows
        elif d[most]['total'] == d[key]['total']:
            most_occur = max(d[most]['top'], d[most]['bot'])
            occur = max(d[key]['top'], d[key]['bot'])
            
            if occur > most_occur:
                most = key
    #Check if an entire row can be the same number
    if d[most]['total'] >= len(tops):
        most_occur = max(d[most]['top'], d[most]['bot'])
        #Check if there were dominoes with same numbers on top and bottom row
        dupes =  d[most]['total'] - (d[most]['top'] + d[most]['bot'])
        return len(tops) - dupes - most_occur
    else:
        return -1
