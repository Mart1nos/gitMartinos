import simple_draw as sd

sd.resolution = (1500, 800)


for y in range(0, 250, 50):
    x = 450
    for x in range(x, 850, 50):
        start_poin = sd.get_point(x, y)
        end_point = sd.get_point(x + 50, y + 25)
        sd.rectangle(start_poin, end_point, width=1)
for y in range(25, 250, 50):
    x = 425
    for x in range(x, 850, 50):
        start_poin = sd.get_point(x, y)
        end_point = sd.get_point(x + 50, y + 25)
        sd.rectangle(start_poin, end_point, width=1)


point_0 = sd.get_point(425, 0)
point_1 = sd.get_point(875, 0)
v1 = sd.get_vector(start_point=point_0, angle=90, length=250, width=5)
v1.draw()
v2 = sd.get_vector(start_point=point_1, angle=90, length=250, width=5)
v2.draw()

point_2 = sd.get_point(400, 250)
v3 = sd.get_vector(start_point=point_2, angle=0, length=500, width=10)
v3.draw(color=sd.COLOR_RED)
v4 = sd.get_vector(start_point=v3.end_point, angle=150, length=290, width=10)
v4.draw(color=sd.COLOR_RED)
v5 = sd.get_vector(start_point=v4.end_point, angle=210, length=290, width=10)
v5.draw(color=sd.COLOR_RED)

sd.pause()


