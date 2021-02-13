x = 0
for number in range(1, 101):
    if number % 2 == 0:
        x += number
    else:
        pass
print(x)

#The Way I Mad ^
#Model way

y = 0
for number in range(2, 101, 2):
    y += number
print(y)