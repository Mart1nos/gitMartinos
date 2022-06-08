def foo(x, y=0, z=0):
    return 100*x + 10*y + 1*z


print(foo(1, 2 ,3))
print(foo(z=1, x=2, y=3)) # именованные параметры
print(foo(1, 2)) # если z=0
print((foo(7))) # Если y=0 z=0