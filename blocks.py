blocks = int(input("Enter the number of blocks: "))

height = 0

rows = 1

while rows <= blocks:

    height += 1
    # is the height +1
    blocks -= rows
    #blocks - rows 
    if blocks <= rows:
        break

    # while the rows are less than the blocks keep going.
    # if the rows become greater than the blocks stop 
    rows += 1

    
print("The height of the pyramid:", height)