# Get-SVG-fill-colors
Get the list of fill colors used on a SVG file. These are colors used to fill the paths.

When I am using the MANIM python libary and I create a SVGMobject, it destroys all the SVG's style (fill colors, stroke_width,
stroke_color, etc).
I created this script to get the fill_colors from the original svg. Colors that are not in HEX format will be discarded.

Copy the code from get_colors.py and then type:

colors = get_colors(YOUR_SVG_PATH)

The variable colors will save a list of colors used to fill the paths on the original SVG file. Then you can use it to manually
fill your paths on MANIM.
