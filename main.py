# Create a list of conataining tuples of rgb vallues oof the most used colors in a jpg image
import colorgram

colors = colorgram.extract("The-Hirst-Painting/test-image.jpg", 10)

rgb_colors = []
for color in colors:
    rgb = color.rgb  # NamedTuple of (r, g, b)
    rgb_colors.append((rgb.r, rgb.g, rgb.b))

print(rgb_colors)
