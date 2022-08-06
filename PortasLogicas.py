def and_(string = "0"):
    try:
        if "0" in string:
            return "0"
        return "1"
    except:
        return "0"


def or_(string = "0"):
    try:
        if "1" in string:
            return "1"
        return "0"
    except:
        return "0"


def xor(string = "00"):
    try:
        if len(string)!= 2:
            return "0"
        elif string[0] == string[1]:
            return "0"
        else:
            return "1"
    except:
        return "0"


def inversor(string = "1"):
    try:
        if string == "0":
            return "1"
        else:
            return "0"
    except:
        return "0"


def nand(string = "1"):
    try:
        return inversor(and_(string))
    except:
        return "0"


def nor(string = "0"):
    try:
        return inversor(or_(string))
    except:
        return "0"


def xnor(string = "01"):
    try:
        return inversor(xor(string))
    except:
        return "0"

