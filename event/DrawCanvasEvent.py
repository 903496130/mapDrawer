import entity.MapData as mapData
import util.colorUtil as colorUtil
import util.commonUtil as commonUtil
import config.config as config

brashMap = []


def updateMapArray(canvas, x, y, color):
    if x < 0 or x >= config.mapSize or y < 0 or y >= config.mapSize:
        return
    originValue = mapData.mapArray[x][y]

    if not config.penMode:
        key = "{} {}".format(x, y)
        if key not in brashMap:
            brashMap.append(key)
            color = colorUtil.getColorWithOpacity(originValue)
        else:
            return

    if originValue != color:
        mapData.changeMapColor(canvas, x, y, color)


def handleMouseMoveEvent(canvas, event):
    blockWidthAndHeight = commonUtil.getUnitLength(canvas)
    # 以坐标为中心 画一个10*10的绿色正方形

    x = int(event.x // blockWidthAndHeight)
    y = int(event.y // blockWidthAndHeight)

    updateMapArray(canvas, x, y, config.currentPenColor)


def handleMouseReleaseEvent(canvas, event):
    global brashMap
    brashMap = []
