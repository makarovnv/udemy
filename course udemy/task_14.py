x = 0
for i in range(10, 31, 2):
x += i
print(x)

x = 0
for i in range(31):
if i >= 10 and i % 2 == 0:
x += i
print(x)

x = int(input('Введи число больше 0: '))
for i in range(x):
print('Hello!')