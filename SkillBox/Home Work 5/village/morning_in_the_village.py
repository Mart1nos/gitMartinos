import simple_draw as sd

sd.resolution = (1500, 800)

def people(): # Человечек
    left = sd.get_point(970, 190)
    right = sd.get_point(1100, 290)
    sd.ellipse(left_bottom=left, right_top=right, color=sd.COLOR_DARK_PURPLE, width=2)

    point_0 = sd.get_point(1035, 100)
    v1 = sd.get_vector(start_point=point_0, angle=90, length=90, width=2)
    v1.draw(color=sd.COLOR_DARK_PURPLE)
    point_1 = sd.get_point(1035, 170)
    v2 = sd.get_vector(start_point=point_1, angle=225, length=50, width=2)
    v2.draw(color=sd.COLOR_DARK_PURPLE)
    point_2 = sd.get_point(1035, 170)
    v3 = sd.get_vector(start_point=point_2, angle=315, length=50, width=2)
    v3.draw(color=sd.COLOR_DARK_PURPLE)
    point_3 = sd.get_point(1035, 100)
    v4 = sd.get_vector(start_point=point_3, angle=235, length=60, width=2)
    v4.draw(color=sd.COLOR_DARK_PURPLE)
    point_4 = sd.get_point(1035, 100)
    v5 = sd.get_vector(start_point=point_4, angle=305, length=60, width=2)
    v5.draw(color=sd.COLOR_DARK_PURPLE)

    center_1 = sd.get_point(1010, 250)
    sd.circle(center_position=center_1, radius=5, color=sd.COLOR_DARK_PURPLE, width=2)
    center_2 = sd.get_point(1060, 250)
    sd.circle(center_position=center_2, radius=5, color=sd.COLOR_DARK_PURPLE, width=2)

    point_5 = sd.get_point(1025, 215)
    v6 = sd.get_vector(start_point=point_5, angle=0, length=20, width=2)
    v6.draw(color=sd.COLOR_DARK_PURPLE)
    v7 = sd.get_vector(start_point=v6.end_point, angle=25, length=20, width=2)
    v7.draw(color=sd.COLOR_DARK_PURPLE)
    v8 = sd.get_vector(start_point=v6.start_point, angle=155, length=20, width=2)
    v8.draw(color=sd.COLOR_DARK_PURPLE)

    left_1 = sd.get_point(0, 0) # Первая точка вниху
    right_1 = sd.get_point(1500, 45) # Вторая точка мы вытягиваем прямоугольник
    sd.rectangle(left_bottom=left_1, right_top=right_1, color=sd.COLOR_GREEN, width=0)

people()

def rainbow(): # Радуга
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    sd.resolution = (1500, 800)

    point = sd.get_point(410, -50)
    radius = 1100

    for colors in rainbow_colors:
        radius += 10
        sd.circle(center_position=point, radius=radius, width=10, color=colors)

rainbow()

def snowflakes(): # Снежинки
    i = 0
    while i < 41:
        x = sd.random_number(0, 400)
        y = sd.random_number(75, 100)
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=30)
        i += 1

snowflakes()

def sun(): # Солнце
    center = sd.get_point(250, 670)
    sd.circle(center_position=center, radius=50, color=sd.COLOR_YELLOW, width=0)

    point_0 = sd.get_point(250, 670)
    v1 = sd.get_vector(start_point=point_0, angle=90, length=100, width=6)
    v1.draw(color=sd.COLOR_YELLOW)
    v2 = sd.get_vector(start_point=point_0, angle=270, length=100, width=6)
    v2.draw(color=sd.COLOR_YELLOW)
    v3 = sd.get_vector(start_point=point_0, angle=0, length=100, width=6)
    v3.draw(color=sd.COLOR_YELLOW)
    v4 = sd.get_vector(start_point=point_0, angle=180, length=100, width=6)
    v4.draw(color=sd.COLOR_YELLOW)
    v5 = sd.get_vector(start_point=point_0, angle=45, length=100, width=6)
    v5.draw(color=sd.COLOR_YELLOW)
    v6 = sd.get_vector(start_point=point_0, angle=135, length=100, width=6)
    v6.draw(color=sd.COLOR_YELLOW)
    v7 = sd.get_vector(start_point=point_0, angle=225, length=100, width=6)
    v7.draw(color=sd.COLOR_YELLOW)
    v8 = sd.get_vector(start_point=point_0, angle=315, length=100, width=6)
    v8.draw(color=sd.COLOR_YELLOW)

sun()

def draw_branches(point, angle, length): # Большое дерево
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw(color=sd.COLOR_GREEN)
    next_point = v1.end_point
    next_angle = angle - 30
    next_angle_2 = angle + 30
    next_length = length * .75
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    draw_branches(point=next_point, angle=next_angle_2, length=next_length)

point_0 = sd.get_point(1170, 45) # Начальная точка по x и y
draw_branches(point=point_0, angle=90, length=120)

def draw_branches(point, angle, length): # Маленькое дерево
    if length < 3:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - 30
    next_angle_2 = angle + 30
    next_length = length * .75
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    draw_branches(point=next_point, angle=next_angle_2, length=next_length)

point_1 = sd.get_point(1250, 70)
draw_branches(point=point_1, angle=90, length=35)

def wall():
    for y in range(45, 295, 50):
        x = 450
        for x in range(x, 850, 50):
            start_poin = sd.get_point(x, y)
            end_point = sd.get_point(x + 50, y + 25)
            sd.rectangle(start_poin, end_point, width=1)
    for y in range(70, 295, 50):
        x = 425
        for x in range(x, 850, 50):
            start_poin = sd.get_point(x, y)
            end_point = sd.get_point(x + 50, y + 25)
            sd.rectangle(start_poin, end_point, width=1)

    point_0 = sd.get_point(425, 45)
    point_1 = sd.get_point(875, 45)
    v1 = sd.get_vector(start_point=point_0, angle=90, length=250, width=5)
    v1.draw()
    v2 = sd.get_vector(start_point=point_1, angle=90, length=250, width=5)
    v2.draw()

    point_2 = sd.get_point(400, 295)
    v3 = sd.get_vector(start_point=point_2, angle=0, length=500, width=10)
    v3.draw(color=sd.COLOR_RED)
    v4 = sd.get_vector(start_point=v3.end_point, angle=150, length=290, width=10)
    v4.draw(color=sd.COLOR_RED)
    v5 = sd.get_vector(start_point=v4.end_point, angle=210, length=290, width=10)
    v5.draw(color=sd.COLOR_RED)

wall()



sd.pause()