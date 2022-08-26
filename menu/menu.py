import tkinter
import config.config as config


def changePenColorToRed():
    config.currentPenColor = "#FF0000"
    print("changePenColorToRed:", config.currentPenColor)


def changePenColorToGreen():
    config.currentPenColor = "#00FF00"
    print("changePenColorToGreen:", config.currentPenColor)


def changePenColorToYellow():
    config.currentPenColor = "#FFFF00"
    print("changePenColorToYellow:", config.currentPenColor)


def changePenColorToBlue():
    config.currentPenColor = "#0000FF"
    print("changePenColorToBlue:", config.currentPenColor)


def changePenModeToPen():
    config.penMode = True
    print("changePenModeToPen:", config.penMode)


def changePenModeToBrush():
    config.penMode = False
    print("changePenModeToBrush:", not config.penMode)


def changeBackgroundColorToBlack():
    config.backgroundColor = "#000000"
    print("changeBackgroundColorToBlack:", config.backgroundColor)


def changeBackgroundColorToWhite():
    config.backgroundColor = "#FFFFFF"
    print("changeBackgroundColorToWhite:", config.backgroundColor)


def addMenuToWindow(windows):
    # 创建菜单栏
    menu = tkinter.Menu(windows)

    colorMenu = tkinter.Menu(menu, tearoff=0)

    colorMenu.add_radiobutton(label="红色", command=changePenColorToRed)
    colorMenu.add_radiobutton(label="绿色", command=changePenColorToGreen)
    colorMenu.add_radiobutton(label="黄色", command=changePenColorToYellow)
    colorMenu.add_radiobutton(label="蓝色", command=changePenColorToBlue)

    backgroundMenu = tkinter.Menu(menu, tearoff=0)
    backgroundMenu.add_radiobutton(label="黑色", command=changeBackgroundColorToBlack)
    backgroundMenu.add_radiobutton(label="白色", command=changeBackgroundColorToWhite)

    penModeMenu = tkinter.Menu(menu, tearoff=0)
    penModeMenu.add_radiobutton(label="画笔模式", command=changePenModeToPen)
    penModeMenu.add_radiobutton(label="刷子模式", command=changePenModeToBrush)

    menu.add_cascade(label="颜色选择", menu=colorMenu)
    menu.add_cascade(label="画笔模式", menu=penModeMenu)

    menu.add_cascade(label="背景颜色", menu=backgroundMenu)

    windows.config(menu=menu)

    pass
