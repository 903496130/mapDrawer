import config.config as config
import util.arrayUtil as arrayUtil

opacityArray = arrayUtil.createArray(config.mapSize, config.mapSize, 1)


def changeMapOpacity(x, y, opacity):
    opacityArray[x][y] *= opacity


def getMapOpacity(x, y):
    return opacityArray[x][y]
