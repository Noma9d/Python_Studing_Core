def get_grade(key):

    a = {"F" : 1,"FX" : 2, "E" : 3, "D" :3, "C" : 4, "B" : 5, "A" : 5}
       
    for i in a.keys():
        if key == i:
            return a[i]


def get_description(key):
    a = {"F" : 'Unsatisfactorily',"FX" : 'Unsatisfactorily', "E" : 'Enough', "D" :'Satisfactorily', "C" : 'Good', "B" : 'Very good', "A" : 'Perfectly'}

    for i in a.keys():
        if key == i:
            return a[i]
        

print(get_grade('A'))

print(get_description('A'))
