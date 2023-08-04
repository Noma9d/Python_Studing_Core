def game(terra, power):
    
    for i in terra:

        for j in i:
            if power >= j:
                power += j
            else:
                break
    
    return power

print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))