def get_colors(svg):
    svg = open(svg, "r") #open the svg
    svg = svg.read()     #read the svg 

    colors = [] 

    while True:
        try:
            color_index = svg.index(r'fill="#') + 6 #get the index of the caracter #
            color = svg[color_index:color_index+7]  #get the hex color, e.g. #e5646e
            if color not in colors:                 #check if the color already exists
                if not any([not letter.isalpha() and not letter.isdigit() for letter in color[1:]]): #assert there is no special characters on the color
                    colors.append(color)                                                             #color ok, append color
            svg = svg[color_index+7:]                                                                #svg restarts from the end of last color
        except:                                                                                      #error means there is no color left
            break

    return colors
