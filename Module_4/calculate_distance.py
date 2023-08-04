points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) == 0 or len(coordinates) == 1:
        return 0
    
    point = []
    
    for i in range(len(coordinates)-1):
        if coordinates[i] < coordinates[i + 1]:
            point.append((coordinates[i], coordinates[i+1]))
        else:
            point.append((coordinates[i+1], coordinates[i]))
    
    distance = 0
    
    for item in points.keys():
        for j in point:
            if item == j:
                distance += points[item]

    distance = round(distance, 1)

    return distance

print(calculate_distance([0, 1, 3, 2, 0, 2]))