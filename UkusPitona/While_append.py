print("Добрый день, давай напишем список наших покупок?")
b = []
running = True

while running:
    a = input("Что нам нужно купить? ")
    if a == "выход":
        break
    b.append(a)
    print("В нашем холодильнике есть:", *b)