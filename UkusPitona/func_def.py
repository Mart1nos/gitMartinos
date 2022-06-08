a = int(input())
b = int(input())

def develop(num1, num2):
    function = num1 * num2
    if function >= 1000:
        print(function)
    else:
        print(num1 + num2)

develop(a, b)