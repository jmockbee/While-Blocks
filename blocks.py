blocks = int(input("Enter the number of blocks: "))

height = 0

rows = 1

while rows <= blocks:

    height += 1
    blocks -= rows
    if blocks <= rows:
        break
    rows += 1

    
print("The height of the pyramid:", height)