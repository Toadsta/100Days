student_scores = {
  "Echo": 81,
  "Hunter": 78,
  "Tech": 99, 
  "Crosshair": 74,
  "Wrecker": 62,
}

student_grades = {
}

for key in student_scores:
    gradeNum = student_scores[key]
    name = key
    if gradeNum > 90:
        gradeLet = "A"
    elif gradeNum > 80 and gradeNum < 91:
        gradeLet = "B"
    elif gradeNum > 70 and gradeNum <81:
        gradeLet = "C"
    else:
        gradeLet = "F"
    student_grades[name] = gradeLet
    


print(student_grades)