
def _1d(str_: str, separator: str = "\n") -> list:
    list_ = list()

    temp_x = []
    for x in str_.split(separator):
        temp_x += x
    list_ += temp_x

    return list_


def _2d(str_: str, separator: str = "\n") -> list:
    list_ = list()

    temp_y = []
    for y in str_.split(separator):
        temp_x = []
        for x in y:
            temp_x += x
        temp_y += [temp_x]
    list_ += temp_y

    return list_


def _3d(str_: str, separator: str = "\n") -> list:
    list_ = list()

    temp_z = []
    for z in str_.split(separator):
        temp_y = []
        for y in z:
            temp_x = []
            for x in y:
                temp_x += x
            temp_y += [temp_x]
        temp_z += [temp_y]
    list_ += [temp_z]

    return temp_z
