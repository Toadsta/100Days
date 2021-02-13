studentHeight = input("Input a list of student heights ").split()
for studentNum in range(0, len(studentHeight)):
  studentHeight[studentNum] = int(studentHeight[studentNum])
#harder version using for loops
#this script below adds the height to the totalheight for each item in the list.
totalHeight = 0
for height in studentHeight:
    totalHeight += height
#the thing below adds one to the total number each time for each item in the list.
totalNumber = 0
for number in studentHeight:
    totalNumber += 1
#below does the mean of the thing above
averageHeight = round(totalHeight/totalNumber)
print(f"The average height of all students is {averageHeight}cm")

#easy version using sum and len
#sumHeight = sum(studentHeight)
#avgHeight = sumHeight/len(studentHeight)
#roundAvgHeight = round(avgHeight)
#print(f"The average height of all students is {roundAvgHeight}cm")