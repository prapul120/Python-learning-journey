rows = 10
cols = 10

width = len(str(rows * cols))

for i in range(1,rows + 1):
    for j in range(cols):
        num = i + j * rows
        print(f"{num:{width}d}",end= '  ')
    print()