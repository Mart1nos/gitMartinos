def main():
    x, y = 300, 400
    width, height = 200, 200
    draw_house()


def draw_house(x, y, width, height):
    '''
    Нарисовать домик ширины width и высоты height от опорной точки (х, у).
    которая находится с середине нижней точки фундамента.
    :param x: координата х середины домика
    :param y: координата у низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: none
    '''
    print("Рисую домик....", x, y, width, height)
    foundation_height = 0.05 * height
    walls_widht = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_height, walls_widht)
    draw_house_roof(x, y, foundation_height - walls_height, width, roof_height)

def draw_house_foundation(x, y, width, haight):
    print("Рисую основание....", x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    print("Рисую стены....", x, y, width, height)
    pass



def draw_house_roof(x, y, width, height):
    print("Рисую крышу....", x, y, width, height)
    pass


main()
