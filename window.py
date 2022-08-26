import tkinter
import config.config as config
import canvas.drawCanvas as drawCanvas
import canvas.showCanvas as showCanvas
import event.MainWindowEvent as mainWindowEvent
import menu.menu as menu


# 添加窗口组件
def addComponent(window):
    # 添加左侧画布
    leftCanvas = drawCanvas.addCanvasToWindow(window)
    drawCanvas.fullCanvasWithBlock(config.backgroundColor)

    # 添加右侧画布
    rightCanvas = showCanvas.addCanvasToWindow(window)
    showCanvas.drawNumbers(rightCanvas)

    # 添加菜单栏
    menu.addMenuToWindow(window)

    # 给窗口添加一个编辑框 右侧是两个按钮,一个是打开按钮,点击可以选择本地文件;一个是保存按钮,点击可以保存文件
    # 添加编辑框
    # editText = tkinter.Text(window, width=config.editTextWidth, height=config.editTextHeight)
    # editText.pack(side='right')
    # # 添加打开按钮
    # openButton = tkinter.Button(window, text='打开', command=lambda: mainWindowEvent.openFile(editText))
    # openButton.pack(side='right')
    # # 添加保存按钮
    # saveButton = tkinter.Button(window, text='保存', command=lambda: mainWindowEvent.saveFile(editText))
    # saveButton.pack(side='right')




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
