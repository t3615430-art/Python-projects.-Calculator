a = input("Введи первое число: ")
print(a)
b = input("Введи второе число: ")
action = input("Выбери действие (+, -, *, /): ")
if action == "+":
    print(float(a) + float(b))
elif action == "-":
    print(float(a) - float(b))
elif action == "*":
    print(float(a) * float(b))
elif action == "/":
    print(float(a) / float(b))
