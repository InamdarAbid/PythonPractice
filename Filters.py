def test_funct(grade):
    return grade != 'F' 
grades = ['A','B','F','A','C','E']
print(list(filter(test_funct,grades)))

#Using for loop
filter_grades = []
for grade in grades:
    if grade != 'F':
        filter_grades.append(grade)
print(filter_grades)

#Using comprehension 
print([grade for grade in grades if grade != 'F'])