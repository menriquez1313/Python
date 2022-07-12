###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('The Hirst Painting Project/image.jpg', 30)
for color in colors:
    #rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    
print(rgb_colors)