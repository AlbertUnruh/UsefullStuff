
def _1d(list_: list, merger: str = "\n") -> str:
    str_ = str()

    for x in list_:
        str_ += x
    str_ += merger

    return str_[:-1]


def _2d(list_: list, merger: str = "\n") -> str:
    str_ = str()

    for y in list_:
        for x in y:
            str_ += x
        str_ += merger

    return str_[:-1]


def _3d(list_: list, merger: str = "\n") -> str:
    str_ = str()

    for z in list_:
        for y in z:
            for x in y:
                str_ += x
            str_ += merger

    return str_[:-1]

