import simple_draw as sd

sd.resolution = (1500, 800)

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

sd.pause()