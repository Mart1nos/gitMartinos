import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1500, 800)

point = sd.get_point(410, -50)
radius = 1100

for colors in rainbow_colors:
    radius += 10
    sd.circle(center_position=point, radius=radius, width=10, color=colors)

sd.pause()