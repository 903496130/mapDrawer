import config.config as config
import tkinter


# 根据百分比字符串获取窗口高度
def getHeight(window, height):
    height = int(height.replace('%', ''))
    return int(window.winfo_height() * height / 100)


# 根据百分比字符串获取窗口宽度
def getWidth(window, width):
    width = int(width.replace('%', ''))
    return int(window.winfo_width() * width / 100)


# 获取单位宽/高度
def getUnitLength(leftCanvas):
    # 获取canvas的高度、宽度
    return leftCanvas.winfo_reqheight() / config.mapSize
