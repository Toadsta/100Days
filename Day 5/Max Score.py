studentScore = input("Input a list of student scores ").split()
for studentNum in range(0, len(studentScore)):
  studentScore[studentNum] = int(studentScore[studentNum])

#this script starts with the first score, it is then compared to second if second is bigger that becomes the listScore and this continues until all mumbers have been compared
listScore = studentScore[0]
for maxScore in studentScore:
    if listScore > maxScore:
        maxScore = listScore
print(f"The highest score in the class is: {maxScore}")

#easier way
#print(max(studentScore))