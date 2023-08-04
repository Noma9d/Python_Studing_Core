def solve_riddle(riddle, word_length, start_letter, reverse=False):
    start = riddle.find(start_letter)
    if start == -1:
        return ''
    
    if reverse == False:
        s = start + word_length
        return riddle[start:s]
    elif reverse == True:
        result = riddle[start::-1]
        return result[0:word_length]

        
            
                
            
                
print(solve_riddle('mi1rewopret', 5, 'p', reverse=True))