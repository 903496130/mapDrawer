import config.config as config
import util.commonUtil as commonUtil
import util.arrayUtil as arrayUtil

mapArray = arrayUtil.createArray(config.mapSize, config.mapSize, config.backgroundColor)


def changeMapColor(canvas, x, y, color):
    blockWidthAndHeight = commonUtil.getUnitLength(canvas)
    mapArray[x][y] = color
    canvas.create_rectangle(x * blockWidthAndHeight, y * blockWidthAndHeight,
                            (x + 1) * blockWidthAndHeight,
                            (y + 1) * blockWidthAndHeight, fill=color, outline=color)
    if config.debug:
        print('x:', x, 'y:', y, 'color:', color)
