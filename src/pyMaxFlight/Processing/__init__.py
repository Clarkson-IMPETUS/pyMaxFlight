import pandas as pd
import bisect

def loadData(csvPath):
    data = pd.DataFrame(pd.read_csv(csvPath))
    data["time"] = data["time"] / 1000.0 # msec -> sec
    data["pitch_real"] = -data["pitch_real"] 
    return data

def getRelativeTimes(data):
    timeStart = data["time"][0]
    timesRelative = list(
        map(
            lambda x: x - timeStart,
            data["time"]
        )
    )
    return timeStart, timesRelative

def getTimeIndex(data, timeCurrent):
    return bisect.bisect_left(list(data["time"]), timeCurrent)

def getValueAtIndex(data, index, axis="roll", realOrTarget = "real"):
    return data[f"{axis}_{realOrTarget}"][index]

def getValueAtTime(data, timeCurrent, axis="roll", realOrTarget = "real"):
    return getValueAtIndex(
        data,
        getTimeIndex(data, timeCurrent),
        axis,
        realOrTarget
    )

def getModuloOffset(
    obj: list or pd.DataFrame,
    key: str = None
) -> float:
    if not (key is None):
        obj = obj[key]
        key = None

    valFirst = obj[0]

    valFirstSign = 1 if valFirst > 0 else -1
    valFirst *= valFirstSign

    offset = 0
    while (valFirst + offset) > 180:
        offset -= 360

    return offset

def modulateStartAndOffset(
    obj: list or pd.DataFrame,
    key: str = None
) -> None:
    """
    Determines angular modulation from the first value in the data.
    (eg. If the first value was 400, it would be modulated to 40.)
    This offset is then applied to all data.

    This modifies `obj` in place.
    If this isn't desired, copy it manually first.
    """

    if not (key is None):
        obj = obj[key]
        key = None

    obj += getModuloOffset(obj, key)

def removeModulation(
    obj: list or pd.DataFrame,
    key: str = None
) -> None:
    """
    Removes angular modulation (in degrees) from data. Accepts both
    standard lists and Pandas dataframes (using a key to a column).

    This modifies `obj` in place.
    If this isn't desired, copy it manually first.
    """
    
    value_prev = None
    offset = 0

    iMax = len(obj)

    if not (key is None):
        obj = obj[key]
        key = None

    for i in range(iMax):
        value = obj[i]
        if not (value_prev is None):
            if (value < -90) and (value_prev > 90):
                offset += 360
            elif (value > 90) and (value_prev < -90):
                offset -= 360
        obj[i] += offset
        value_prev = value