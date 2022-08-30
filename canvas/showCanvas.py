import io
import tkinter
from PIL import Image, ImageTk
import config.config as config
import util.commonUtil as commonUtil
import entity.MapData as MapData
import time

canvas = None
canvasBackup = None
canvasImage = None


# 创建备用canvas
def createBackupCanvas(window):
    global canvasBackup
    # 创建备份canvas
    canvasBackup = tkinter.Canvas(window, bg='#FFFFFF', height=commonUtil.getHeight(window, "100%") - 20,
                                  width=commonUtil.getHeight(window, "100%") - 20)
    canvasBackup.place(x=commonUtil.getHeight(window, "200%") - 50, y=5)


# 绘制canvas
def addCanvasToWindow(window):
    global canvas
    canvas = tkinter.Canvas(window, bg='#FFFFFF', height=commonUtil.getHeight(window, "100%") - 20,
                            width=commonUtil.getHeight(window, "100%") - 20)
    canvas.place(x=commonUtil.getHeight(window, "100%") - 50, y=5)
    createBackupCanvas(window)
    return canvas


# 绘制备用canvas
def drawBackupCanvas():
    global canvasBackup
    # 在Canvas中画满倾斜的直线
    maxLength = canvas.winfo_reqheight()
    skewLineWidth = config.skewLineWidth
    skewLineSpace = config.skewLineSpace
    skewLineColor = config.skewLineColor

    startX, startY, endX, endY = getPosition(0, 0)
    mapSize = config.mapSize
    x = startX
    y = startY
    unitLength = canvas.winfo_reqheight() / mapSize * config.picSize
    # canvas 画满正方形
    for i in range(mapSize):
        for j in range(mapSize):
            # 画宽度为2的矩形
            canvasBackup.create_rectangle(x, y, x + unitLength, y + unitLength, outline=config.borderColor, width=2,
                                          fill="#6c1606")
            x += unitLength
        x = startX
        y += unitLength

    x = 0
    y = 0

    # canvas 画一条直线
    while x <= 2 * maxLength and y <= 2 * maxLength:
        canvasBackup.create_line(x, 0, 0, y, fill=skewLineColor, width=skewLineWidth)
        x += skewLineSpace
        y += skewLineSpace
        # break


# 主canvas创建border
def drawInnerBorder():
    picSize = config.picSize
    height = canvas.winfo_reqheight()
    length = height * picSize
    unitLength = length / config.mapSize
    startX = height * (1 - picSize) / 2
    startY = height * (1 - picSize) / 2

    canvas.create_rectangle(startX, startY,
                            startX + length,
                            startY + length,
                            fill='#FFFFFF', outline='#000000', width=2)
    lineWith = unitLength * 0.5
    for i in range(config.mapSize):
        y = startY + i * unitLength + unitLength / 2
        canvas.create_line(startX, y, startX - lineWith, y, fill='#000000', width=2)
        # 在线段的左边画文字
        canvas.create_text(startX - lineWith - unitLength / 2, y, text=i, fill='#000000',
                           font=('Arial', config.showCanvasNumFontSize))
    for i in range(config.mapSize):
        x = startX + i * unitLength + unitLength / 2
        y = startY + length
        canvas.create_line(x, y, x, y + lineWith, fill='#000000', width=2)
        # 在线段的下面画文字
        canvas.create_text(x, y + lineWith + unitLength / 2 + 5, text=i, fill='#000000',
                           font=('Arial', config.showCanvasNumFontSize))


def drawNumbers():
    drawInnerBorder()
    # canvas.create_text(x, y, text=number, fill='#000000')


def getPosition(x, y):
    picSize = config.picSize
    height = canvas.winfo_reqheight()
    length = height * picSize
    unitLength = length / config.mapSize
    startX = height * (1 - picSize) / 2 + x * unitLength
    startY = height * (1 - picSize) / 2 + y * unitLength
    endX = startX + unitLength
    endY = startY + unitLength
    return startX, startY, endX, endY


def yellowToBlock():
    global canvas
    array = MapData.mapArray
    # 遍历array,如果array[i][j]=='#FFFF00'
    for i in range(config.mapSize):
        for j in range(config.mapSize):
            if array[i][j] == '#FFFF00':
                drawPic(i, j, '#000000')
                picSize = config.picSize
                height = canvas.winfo_reqheight()
                length = height * picSize
                unitLength = length / config.mapSize
                startX, startY, endX, endY = getPosition(i, j)
                # copyBackupToCanvas(startX, startY, unitLength)


def drawSkewLine(startX, startY, endX, endY):
    skewLineWidth = config.skewLineWidth
    skewLineSpace = config.skewLineSpace
    skewLineColor = config.skewLineColor

    x = startX
    y = startY
    count = 0

    # # canvas 画一条直线
    while x <= endX and y <= endY:
        canvas.create_line(startX, y, x, startY, fill=skewLineColor, width=skewLineWidth)
        if count != 0:
            canvas.create_line(x, endY, endX, y, fill=skewLineColor, width=skewLineWidth)
        x += skewLineSpace
        y += skewLineSpace
        count += 1
        # break


def drawPic(x, y, colorType):
    # 判断是否为红绿蓝黄
    startX, startY, endX, endY = getPosition(x, y)
    if config.debug:
        print(startX, startY, endX, endY)

    if colorType == '#FF0000':  # 红色
        canvas.create_rectangle(startX, startY, endX, endY, outline="#8a210b", fill="#8a210b")
    elif colorType == '#00FF00':  # 绿色
        pass
    elif colorType == '#0000FF':  # 蓝色
        canvas.create_rectangle(startX, startY, endX, endY, outline="#0b0997", fill="#0b0997")
    elif colorType == '#FFFF00':  # 黄色
        canvas.create_rectangle(startX, startY, endX, endY, outline=config.borderColor, fill="#6c1606", width=2)
        drawSkewLine(startX, startY, endX, endY)
