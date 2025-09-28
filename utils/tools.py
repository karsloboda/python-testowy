#1. konwerter temperatur
from unittest import result, case


def convert_temp(value, format = "K"):
    match(format):
        case "K":
            return round(value, 2)
        case "C":
            result = value - 273.15
            return round(result, 2)
        case "F":
            result = (value - 273.15) * 9/5 + 32
            return round(result, 2)

#2. konwerter wiatru
def convert_wind(value, format = "MS"):
    match(format):
        case "MS":
            return round(value, 2)
        case "KM":
            result = value * 3.6
            return round(result, 2)