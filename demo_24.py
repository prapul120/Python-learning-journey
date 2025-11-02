#for loops = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
hello = []

for i in range(start,end+1):
    j = str(i)
    hi = hello.append(i)

print(hello[::2])

