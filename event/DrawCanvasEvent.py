import entity.MapData as mapData
import util.colorUtil as colorUtil
import util.commonUtil as commonUtil
import canvas.drawCanvas as drawCanvas
import canvas.showCanvas as showCanvas
import config.config as config
import entity.OpacityData as opacityData

brashMap = []

canvas = None

def updateMapArray(canvas, x, y, color):
    if x < 0 or x >= config.mapSize or y < 0 or y >= config.mapSize:
        return

    originValue = mapData.mapArray[x][y]
    blockOpacity = opacityData.getMapOpacity(x, y) * config.brushOpacity

    if not config.penMode:
        key = "{} {}".format(x, y)
        if key not in brashMap:
            brashMap.append(key)
            color = colorUtil.getColorWithOpacity(originValue, blockOpacity)
        else:
            return
    if originValue != color:
        mapData.changeMapColor(canvas, x, y, color)
        showCanvas.drawPic(x, y,config.currentPenColor)


def handleMouseMoveEvent(canvas, event):
    blockWidthAndHeight = commonUtil.getUnitLength(canvas)
    x = int(event.x // blockWidthAndHeight)
    y = int(event.y // blockWidthAndHeight)
    updateMapArray(canvas, x, y, config.currentPenColor)


def handleMouseReleaseEvent(canvas, event):
    global brashMap
    brashMap = []
