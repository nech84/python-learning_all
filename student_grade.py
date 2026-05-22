#project 1
students = {
    "James": [81, 77, 90],
    "Sophia": [95, 92, 88],
    "Daniel": [67, 73, 70],
    "Olivia": [58, 61, 55],
    "Ethan": [45, 50, 48],
    "Emma": [89, 84, 91],
    "Liam": [72, 68, 75],
    "Ava": [99, 97, 100],
    "Noah": [63, 59, 65],
    "Mia": [78, 82, 80],
    "Lucas": [54, 57, 52],
    "Charlotte": [86, 88, 84]
}
best_score = 0
best_name =""
for name,scores in students.items():
    total = 0
    for minor_scores in scores:
        total = total + minor_scores
    averages = total/3
    if averages > best_score: #best score
        best_score = averages 
        best_name = name
    if averages >=80:
        Grade = 'A'
    elif averages >=70:
        Grade = 'B'
    elif averages >=60:
        Grade = 'C'
    elif averages>=50:
        Grade = 'D'
    else:
        Grade = 'F'
    print(name,Grade)

print(best_name,best_score,Grade)    #best score