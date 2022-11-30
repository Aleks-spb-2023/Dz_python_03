n = int(input('Введите число '))
f1 = 0
f2 = 1
arr_fib = [f1, f2]

for i in range(2, n + 1):
    f1 , f2 = f2, f1 + f2
    arr_fib.append(f2)

fb = 0
fb2 = 1
c = -1
arr_fib.insert(0, fb2)
for q in range(-1, -n, -1):
    fb, fb2 = fb2, fb + fb2

    arr_fib.insert(0,fb2)
for i in range(0, len(arr_fib) // 2, 2):
    arr_fib[i] = arr_fib[i] * c
print(arr_fib)