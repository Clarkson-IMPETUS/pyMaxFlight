# Interface

[Pymaxflight Index](../../../README.md#pymaxflight-index) /
`src` /
[Pymaxflight](../index.md#pymaxflight) /
Interface

> Auto-generated documentation for [src.pyMaxFlight.Interface](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py) module.

#### Attributes

- `MAKEWPARAM` - From winuser.h: `win32api.MAKELONG`


## MotionClient

[Show source in __init__.py:69](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L69)

Provides an interface to the MaxFlight Motion Client.
Calling commands without the client open will result in an exception.
NEVER use the Motion Client fully unattended.

#### Signature

```python
class MotionClient:
    ...
```

### MotionClient().counterweightBwd

[Show source in __init__.py:259](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L259)

#### Signature

```python
@ifHandleValid
def counterweightBwd(self):
    ...
```

### MotionClient().counterweightFwd

[Show source in __init__.py:255](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L255)

#### Signature

```python
@ifHandleValid
def counterweightFwd(self):
    ...
```

### MotionClient().forceRaised

[Show source in __init__.py:251](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L251)

#### Signature

```python
@ifHandleValid
def forceRaised(self):
    ...
```

### MotionClient().freeze

[Show source in __init__.py:243](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L243)

#### Signature

```python
@ifHandleValid
def freeze(self):
    ...
```

### MotionClient().getCanopyOpen

[Show source in __init__.py:219](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L219)

#### Signature

```python
@ifHandleValid
def getCanopyOpen(self) -> bool:
    ...
```

### MotionClient().getEmergencyStop

[Show source in __init__.py:215](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L215)

#### Signature

```python
@ifHandleValid
def getEmergencyStop(self) -> bool:
    ...
```

### MotionClient().getLeftRaised

[Show source in __init__.py:203](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L203)

#### Signature

```python
@ifHandleValid
def getLeftRaised(self):
    ...
```

### MotionClient().getLiftReal

[Show source in __init__.py:275](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L275)

#### Signature

```python
@ifHandleValid
def getLiftReal(self) -> float:
    ...
```

### MotionClient().getLogRange

[Show source in __init__.py:279](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L279)

#### Signature

```python
@ifHandleValid
def getLogRange(self, low: int = None, high: int = None) -> list[str]:
    ...
```

### MotionClient().getLowered

[Show source in __init__.py:211](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L211)

#### Signature

```python
@ifHandleValid
def getLowered(self) -> bool:
    ...
```

### MotionClient().getPitchMax

[Show source in __init__.py:191](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L191)

#### Signature

```python
@ifHandleValid
def getPitchMax(self) -> int:
    ...
```

### MotionClient().getPitchMin

[Show source in __init__.py:195](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L195)

#### Signature

```python
@ifHandleValid
def getPitchMin(self) -> int:
    ...
```

### MotionClient().getPitchReal

[Show source in __init__.py:267](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L267)

#### Signature

```python
@ifHandleValid
def getPitchReal(self) -> float:
    ...
```

### MotionClient().getPitchTarget

[Show source in __init__.py:187](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L187)

#### Signature

```python
@ifHandleValid
def getPitchTarget(self) -> int:
    ...
```

### MotionClient().getRightRaised

[Show source in __init__.py:207](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L207)

#### Signature

```python
@ifHandleValid
def getRightRaised(self) -> bool:
    ...
```

### MotionClient().getRollMax

[Show source in __init__.py:174](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L174)

#### Signature

```python
@ifHandleValid
def getRollMax(self) -> int:
    ...
```

### MotionClient().getRollMin

[Show source in __init__.py:178](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L178)

#### Signature

```python
@ifHandleValid
def getRollMin(self) -> int:
    ...
```

### MotionClient().getRollReal

[Show source in __init__.py:271](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L271)

#### Signature

```python
@ifHandleValid
def getRollReal(self) -> float:
    ...
```

### MotionClient().getRollTarget

[Show source in __init__.py:170](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L170)

#### Signature

```python
@ifHandleValid
def getRollTarget(self) -> int:
    ...
```

### MotionClient().home

[Show source in __init__.py:263](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L263)

#### Signature

```python
@ifHandleValid
def home(self):
    ...
```

### MotionClient().ifHandleValid

[Show source in __init__.py:141](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L141)

#### Signature

```python
def ifHandleValid(func):
    ...
```

### MotionClient().ifReady

[Show source in __init__.py:156](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L156)

#### Signature

```python
def ifReady(func):
    ...
```

### MotionClient().init

[Show source in __init__.py:79](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L79)

#### Signature

```python
def init(self):
    ...
```

### MotionClient().liftLower

[Show source in __init__.py:231](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L231)

#### Signature

```python
@ifHandleValid
def liftLower(self):
    ...
```

### MotionClient().liftRaise

[Show source in __init__.py:223](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L223)

#### Signature

```python
@ifHandleValid
def liftRaise(self):
    ...
```

### MotionClient().liftStop

[Show source in __init__.py:227](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L227)

#### Signature

```python
@ifHandleValid
def liftStop(self):
    ...
```

### MotionClient().run

[Show source in __init__.py:239](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L239)

#### Signature

```python
@ifHandleValid
def run(self):
    ...
```

### MotionClient().setPitchTarget

[Show source in __init__.py:182](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L182)

#### Signature

```python
@ifHandleValid
@ifReady
def setPitchTarget(self, val: int):
    ...
```

### MotionClient().setRollTarget

[Show source in __init__.py:165](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L165)

#### Signature

```python
@ifHandleValid
@ifReady
def setRollTarget(self, val: int):
    ...
```

### MotionClient().start

[Show source in __init__.py:235](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L235)

#### Signature

```python
@ifHandleValid
def start(self):
    ...
```

### MotionClient().status

[Show source in __init__.py:285](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L285)

#### Signature

```python
@ifHandleValid
def status(self) -> dict:
    ...
```

### MotionClient().stop

[Show source in __init__.py:247](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L247)

#### Signature

```python
@ifHandleValid
def stop(self):
    ...
```



## GetListBoxCount

[Show source in __init__.py:15](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L15)

#### Signature

```python
def GetListBoxCount(hwnd):
    ...
```



## GetListBoxLine

[Show source in __init__.py:18](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L18)

#### Signature

```python
def GetListBoxLine(hwnd, lineNum):
    ...
```



## GetListBoxRange

[Show source in __init__.py:24](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L24)

#### Signature

```python
def GetListBoxRange(hwnd, low: int = None, high: int = None):
    ...
```



## SetSlider

[Show source in __init__.py:34](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L34)

Sets the position of a Win32 slider and triggers any listeners.

#### Signature

```python
def SetSlider(hwndDialog, hwndSlider, val: float, horizontal: bool = True):
    ...
```
