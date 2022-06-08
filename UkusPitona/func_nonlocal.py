def func_outer():
    x = 2
    print('х равно', x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('локальное х смеилось на', x)

func_outer()