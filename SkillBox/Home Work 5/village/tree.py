import simple_draw as sd

sd.resolution = (1500, 800)
point_0 = sd.get_point(1100, 5) # Начальная точка по x и y

def draw_branches(point, angle, length):
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



draw_branches(point=point_0, angle=90, length=90)

point_1 = sd.get_point(1200, 25)
def draw_branches(point, angle, length):
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



draw_branches(point=point_1, angle=90, length=30)
sd.pause()
