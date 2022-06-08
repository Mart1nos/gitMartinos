colors = ["красный"]

for i in colors:
    if i == "красный":
        colors += ["черный"]
    if i == "черный":
        colors += ["зеленый"]
print(*colors)