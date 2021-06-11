#round of marks

def gradingStudents(grades):
    # Write your code here
    new_grades=[]
    for i in range(len(grades)):
        if grades[i]<=37:
            new_grades.append(grades[i])
        elif grades[i]>37 and (grades[i]+2)%5==0:
            grades[i]+=2
            new_grades.append(grades[i])
        elif (grades[i]+1)%5==0:
            grades[i]+=1
            new_grades.append(grades[i])
        elif grades[i]>37:
            new_grades.append(grades[i])
            
    return new_grades


grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
