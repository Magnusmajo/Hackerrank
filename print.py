"""The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between."""

if __name__ == '__main__':
    n = int(input('Enter the number: '))

for i in range(1, n+1):
    print(i, end="")

#Here is another way, to check it remove the above comment and comment the previous code
# print(*range(1, n + 1), sep='')