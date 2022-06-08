def bar(*args, named_parameter="bar"):
    for arg in args:
        print(named_parameter, 'arg =', arg)

bar()
bar(['the', 'list', 'of', 'strings'])
bar(1, 2, 3)
bar('jelly', 'fish')
bar('jelly', 'fish', named_parameter='SEPARATOR')