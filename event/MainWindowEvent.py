import tkinter
import event.DrawCanvasEvent as drawCanvasEvent
import config.config as config


def resizeEvent(window, height, width):
    if config.debug:
        print('height:', height, 'width:', width)


def openFile(window):
    if config.debug:
        print('openFile')


def saveFile(window):
    if config.debug:
        print('saveFile')
