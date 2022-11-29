n = int(input("Введите число  "))
s = ""
while n != 0:
    last = n % 2
    s += str(last)
    n = n // 2
for i in reversed(s):
    print(i , end = "")