import simple_draw as sd
sd.resolution = (1500, 800)

i = 0
while i < 21:
    x = sd.random_number(100, 300)
    y = sd.random_number(30, 55)
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=30)
    i += 1

sd.pause()
