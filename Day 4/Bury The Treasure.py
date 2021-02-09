 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Top row, then side coloum: ")

top = int(position[0])
side = int(position[1])

map[top-1][side-1] = "x"

print(f"{row1}\n{row2}\n{row3}")
