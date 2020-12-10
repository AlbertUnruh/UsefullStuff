
def _convert(list_: list, merger: str = "\n") -> str:
    str_ = str()

    for x in list_:
        if type(x) == str:
            str_ += x
        else:
            str_ += _convert(list_, merger) + merger
    str_ += merger

    return str_[:-1]
