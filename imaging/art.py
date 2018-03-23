#!/usr/bin/env python3
from math import pi, sin, cos
from PIL import Image

def plotIntensity(exp, pixelsPerUnit = 150):
    canvasWidth = 2 * pixelsPerUnit + 1
    canvas = Image.new("L", (canvasWidth, canvasWidth))

    for py in range(canvasWidth):
        for px in range(canvasWidth):
            # Convert pixel location to [-1,1] coordinates
            x = float(px - pixelsPerUnit) / pixelsPerUnit 
            y = -float(py - pixelsPerUnit) / pixelsPerUnit
            z = exp(x,y)

            # Scale [-1,1] result to [0,255].
            intensity = int(z * 127.5 + 127.5)
            canvas.putpixel((px,py), intensity)

    return canvas

def plotColor(pixelsPerUnit = 150):
    redPlane   = plotIntensity(lambda x, y: sin(pi*x), pixelsPerUnit)
    greenPlane = plotIntensity(lambda x, y: cos(pi*x*y), pixelsPerUnit)
    bluePlane  = plotIntensity(lambda x, y: sin(pi*y), pixelsPerUnit)
    return Image.merge("RGB", (redPlane, greenPlane, bluePlane))

if __name__ == '__main__':
    image = plotColor()
    image.save("img.png", "PNG")

