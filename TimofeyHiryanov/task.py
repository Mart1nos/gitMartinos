a = int(input("Число 1: "))
b = int(input("Число 2: "))
def product(num1,num2):
    resultum = num1 * num2
    if resultum >= 1000:
        print(resultum)
    else:
        print(num1 + num2)

product(a, b)