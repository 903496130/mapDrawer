import config.config as config


def createArray(x, y, content):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(content)
    return array
