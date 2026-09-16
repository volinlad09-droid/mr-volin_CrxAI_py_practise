'''
rows = int(input("enter the number of rows"))

# Upper Half
for i in range(1, rows + 1):
    print("  " * (rows - i) + "* " * (2 * i - 1))

# Lower Half
for i in range(rows - 1, 0, -1):
    print("  " * (rows - i) + "* " * (2 * i - 1))

'''

'''
# 0-1 triangle pattern

rows = int(input("enter the value of rows: "))

for i in range(1, rows + 1):

    for s in range(rows - i):
        print(" ", end=" ")
    
   
    for j in range(1, 2 * i):
        if j % 2 == 1:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
'''

rows = int(input("Enter size of square: "))

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        # Pehli row, aakhri row, pehla column, ya aakhri column par '*' print karo
        if i == 1 or i == rows or j == 1 or j == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Beech ka khali hissa
    print()
