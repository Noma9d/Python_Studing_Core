grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    result = []
    i = 0
    while i < len(students):
        for item, j in students.items():
            i += 1
            k = j.translate(grades)
            result.append(("{:>4}|{:<10}|{:^5}|{:^5}").format(i, item, j, grades[j]))
    
    return result


for el in formatted_grades(students):
    print(el)