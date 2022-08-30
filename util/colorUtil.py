import config.config as config


def getValueByColor(color):
    colorToValue = {
        'red': 1,
        'green': 2,
        'blue': 3,
        'yellow': 4,
        'black': 5,
        'white': 6,
    }
    return colorToValue[color]


def getColorByValue(value):
    valueToColor = {
        1: 'red',
        2: 'green',
        3: 'blue',
        4: 'yellow',
        5: 'black',
        6: 'white',
    }
    return valueToColor[value]


def getColorWithOpacity(color, opacity):
    colorRgb = getColorRgb(color)
    newColorRgb = [int(colorRgb[0] * opacity), int(colorRgb[1] * opacity), int(colorRgb[2] * opacity)]
    return getColorHex(newColorRgb)


# 将颜色转换插RGB数组 如#FFFFFF 转换为 [255, 255, 255]
def getColorRgb(color):
    color = color.lstrip('#')
    lv = len(color)
    return [int(color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]


# 将RGB数组转换成颜色 如[255, 255, 255]转换为 #FFFFFF
def getColorHex(color):
    return '#%02x%02x%02x' % (color[0], color[1], color[2])


if __name__ == "__main__":
    print(getColorRgb('#FFFF00'))
