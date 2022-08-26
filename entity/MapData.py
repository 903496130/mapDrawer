import config.config as config
import util.commonUtil as commonUtil


def createArray(x, y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(config.backgroundColor)
    return array


mapArray = createArray(config.mapSize, config.mapSize)


def changeMapColor(canvas, x, y, color):
    blockWidthAndHeight = commonUtil.getUnitLength(canvas)
    mapArray[x][y] = color
    canvas.create_rectangle(x * blockWidthAndHeight, y * blockWidthAndHeight,
                            (x + 1) * blockWidthAndHeight,
                            (y + 1) * blockWidthAndHeight, fill=color, outline=color)
    if config.debug:
        print('x:', x, 'y:', y, 'color:', color)
