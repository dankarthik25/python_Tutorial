from collections import namedtuple

# list / tuple

color = (55, 155, 255)      # we don't know what it represent (rgb, or hue,staturation, color)...etc

# dictionary

color = {'red': 55, 'green': 155, 'blue': 255}
print(color['red'])


# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
color = Color(blue=255, green=155, red=55)

print color.red
