n= int(input())
students=[]
for _ in range(n):
    name=input() 
    grade=float(input())
    students.append([name,grade])
grades=sorted(set([grade for name, grade in students]))
second_lowest=grades[1]
second_lowest_students=[name for name, grade in students if grade==second_lowest]
for name in sorted(second_lowest_students):
    print(name)
