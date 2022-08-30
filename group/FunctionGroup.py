import tkinter
import config.config as config
import util.commonUtil as commonUtil
import canvas.showCanvas as showCanvas
import event.MainWindowEvent as mainWindowEvent

def addFunctionGroup(window):
    # 创建一个分组
    group = tkinter.LabelFrame(window, text="分组")

    # 分组位置为窗口顶端,宽度为窗口宽度的一半,高度为100px,位于窗口左上角
    group.place(x=7, y=5, width=commonUtil.getHeight(window, "100%") - 70, height=50)

    label = tkinter.Label(group, text="请输入保存文件名:")
    label.pack(side='left')

    # 创建一个文本输入框
    entry = tkinter.Entry(group)
    entry.pack(side='left')

    editText = entry.get()

    openButton = tkinter.Button(group, text='打开', command=lambda: mainWindowEvent.openFile(editText))
    openButton.pack(side='right')

    saveButton = tkinter.Button(group, text='保存', command=lambda: mainWindowEvent.saveFile(editText))
    saveButton.pack(side='right')

    turnButton = tkinter.Button(group, text='转换', command=lambda: showCanvas.yellowToBlock())
    turnButton.pack(side='right')
