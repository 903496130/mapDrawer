import tkinter
import config.config as config
import canvas.drawCanvas as drawCanvas
import canvas.showCanvas as showCanvas
import group.FunctionGroup as functionGroup
import event.MainWindowEvent as mainWindowEvent
import menu.menu as menu


# 添加窗口组件
def addComponent(window):
    # 添加左侧画布
    leftCanvas = drawCanvas.addCanvasToWindow(window)
    drawCanvas.fullCanvasWithBlock(config.backgroundColor)

    # 添加右侧画布
    rightCanvas = showCanvas.addCanvasToWindow(window)
    showCanvas.drawNumbers()
    showCanvas.drawBackupCanvas()

    # 添加菜单栏
    menu.addMenuToWindow(window)

    functionGroup.addFunctionGroup(window)



def startWindow():
    window = tkinter.Tk()
    window.title(config.windowTitle)
    window.geometry(config.windowSize)

    # 注册窗口大小改变事件
    window.bind('<Configure>', lambda event: mainWindowEvent.resizeEvent(window, event.height, event.width))
    # 设置背景颜色
    window.config(bg="#e1dfdd")

    # 窗口在屏幕居中位置出现
    window.update_idletasks()

    addComponent(window)
    window.mainloop()
