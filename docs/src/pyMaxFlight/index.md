# Pymaxflight

[Pymaxflight Index](../../README.md#pymaxflight-index) /
`src` /
Pymaxflight

> Auto-generated documentation for [src.pyMaxFlight](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py) module.

#### Attributes

- `HWND` - Typedef: `int`


- [Pymaxflight](#pymaxflight)
  - [MotionClient](#motionclient)
    - [MotionClient().counterweightBwd](#motionclient()counterweightbwd)
    - [MotionClient().counterweightFwd](#motionclient()counterweightfwd)
    - [MotionClient().forceRaised](#motionclient()forceraised)
    - [MotionClient().freeze](#motionclient()freeze)
    - [MotionClient().getCanopyOpen](#motionclient()getcanopyopen)
    - [MotionClient().getEmergencyStop](#motionclient()getemergencystop)
    - [MotionClient().getLeftRaised](#motionclient()getleftraised)
    - [MotionClient().getLiftReal](#motionclient()getliftreal)
    - [MotionClient().getLogRange](#motionclient()getlogrange)
    - [MotionClient().getLowered](#motionclient()getlowered)
    - [MotionClient().getPitchMax](#motionclient()getpitchmax)
    - [MotionClient().getPitchMin](#motionclient()getpitchmin)
    - [MotionClient().getPitchReal](#motionclient()getpitchreal)
    - [MotionClient().getPitchTarget](#motionclient()getpitchtarget)
    - [MotionClient().getReady](#motionclient()getready)
    - [MotionClient().getRightRaised](#motionclient()getrightraised)
    - [MotionClient().getRollMax](#motionclient()getrollmax)
    - [MotionClient().getRollMin](#motionclient()getrollmin)
    - [MotionClient().getRollReal](#motionclient()getrollreal)
    - [MotionClient().getRollTarget](#motionclient()getrolltarget)
    - [MotionClient().home](#motionclient()home)
    - [MotionClient().liftLower](#motionclient()liftlower)
    - [MotionClient().liftRaise](#motionclient()liftraise)
    - [MotionClient().liftStop](#motionclient()liftstop)
    - [MotionClient().run](#motionclient()run)
    - [MotionClient().setPitchTarget](#motionclient()setpitchtarget)
    - [MotionClient().setRollTarget](#motionclient()setrolltarget)
    - [MotionClient().start](#motionclient()start)
    - [MotionClient().status](#motionclient()status)
    - [MotionClient().stop](#motionclient()stop)

## MotionClient

[Show source in __init__.py:80](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L80)

Provides an interface to the MaxFlight Motion Client.

Calling commands without the client open will result in an exception.
NEVER use the Motion Client fully unattended.

#### Signature

```python
class MotionClient:
    ...
```

### MotionClient().counterweightBwd

[Show source in __init__.py:344](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L344)

Manually moves the counterweight backwards (towards the tail).

This is for troubleshooting and is not necessary to activate under normal circumstances.

#### Signature

```python
@_ifHandleValid
def counterweightBwd(self):
    ...
```

### MotionClient().counterweightFwd

[Show source in __init__.py:335](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L335)

Manually moves the counterweight forwards (towards the cabin).

This is for troubleshooting and is not necessary to activate under normal circumstances.

#### Signature

```python
@_ifHandleValid
def counterweightFwd(self):
    ...
```

### MotionClient().forceRaised

[Show source in __init__.py:326](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L326)

Forces simulator into raised state. (?)

This is for troubleshooting and is not necessary to activate under normal circumstances.

#### Signature

```python
@_ifHandleValid
def forceRaised(self):
    ...
```

### MotionClient().freeze

[Show source in __init__.py:316](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L316)

Locks current target rotation.

#### Signature

```python
@_ifHandleValid
def freeze(self):
    ...
```

### MotionClient().getCanopyOpen

[Show source in __init__.py:272](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L272)

Gets whether the canopy is open.

Note that this does not indicate whether the canopy is locked.
There is currently no way to detect this.

#### Signature

```python
@_ifHandleValid
def getCanopyOpen(self) -> bool:
    ...
```

### MotionClient().getEmergencyStop

[Show source in __init__.py:267](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L267)

Gets whether the emergency stop button is pressed inwards.

#### Signature

```python
@_ifHandleValid
def getEmergencyStop(self) -> bool:
    ...
```

### MotionClient().getLeftRaised

[Show source in __init__.py:252](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L252)

Gets whether the left hydraulic lift has reached the highest position.

#### Signature

```python
@_ifHandleValid
def getLeftRaised(self):
    ...
```

### MotionClient().getLiftReal

[Show source in __init__.py:368](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L368)

Get real lift measurement. (?)

#### Signature

```python
@_ifHandleValid
def getLiftReal(self) -> float:
    ...
```

### MotionClient().getLogRange

[Show source in __init__.py:373](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L373)

Gets range of log messages.

If low is undefined, it will be set to 0.
If high is undefined, it will be set to the last element of the list.
Both indices are inclusive.

#### Signature

```python
@_ifHandleValid
def getLogRange(self, low: int = 0, high: int = None) -> list[str]:
    ...
```

### MotionClient().getLowered

[Show source in __init__.py:262](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L262)

Gets whether the both hydraulic lifts are at the lowest position.

#### Signature

```python
@_ifHandleValid
def getLowered(self) -> bool:
    ...
```

### MotionClient().getPitchMax

[Show source in __init__.py:242](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L242)

Gets maximum pitch position in degrees.

#### Signature

```python
@_ifHandleValid
def getPitchMax(self) -> int:
    ...
```

### MotionClient().getPitchMin

[Show source in __init__.py:247](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L247)

Gets minimum pitch position in degrees.

#### Signature

```python
@_ifHandleValid
def getPitchMin(self) -> int:
    ...
```

### MotionClient().getPitchReal

[Show source in __init__.py:358](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L358)

Get real pitch measurement.

#### Signature

```python
@_ifHandleValid
def getPitchReal(self) -> float:
    ...
```

### MotionClient().getPitchTarget

[Show source in __init__.py:237](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L237)

Gets target pitch position in degrees.

#### Signature

```python
@_ifHandleValid
def getPitchTarget(self) -> int:
    ...
```

### MotionClient().getReady

[Show source in __init__.py:194](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L194)

Returns whether simulator is ready to accept movement commands.

#### Signature

```python
@_ifHandleValid
def getReady(self) -> bool:
    ...
```

### MotionClient().getRightRaised

[Show source in __init__.py:257](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L257)

Gets whether the right hydraulic lift has reached the highest position.

#### Signature

```python
@_ifHandleValid
def getRightRaised(self) -> bool:
    ...
```

### MotionClient().getRollMax

[Show source in __init__.py:216](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L216)

Gets maximum roll position in degrees.

#### Signature

```python
@_ifHandleValid
def getRollMax(self) -> int:
    ...
```

### MotionClient().getRollMin

[Show source in __init__.py:221](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L221)

Gets minimum roll position in degrees.

#### Signature

```python
@_ifHandleValid
def getRollMin(self) -> int:
    ...
```

### MotionClient().getRollReal

[Show source in __init__.py:363](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L363)

Get real roll measurement.

#### Signature

```python
@_ifHandleValid
def getRollReal(self) -> float:
    ...
```

### MotionClient().getRollTarget

[Show source in __init__.py:211](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L211)

Gets target roll position in degrees.

#### Signature

```python
@_ifHandleValid
def getRollTarget(self) -> int:
    ...
```

### MotionClient().home

[Show source in __init__.py:353](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L353)

Sets target roll and pitch to 0.

#### Signature

```python
@_ifHandleValid
def home(self):
    ...
```

### MotionClient().liftLower

[Show source in __init__.py:292](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L292)

Initiates the lowering process.

#### Signature

```python
@_ifHandleValid
def liftLower(self):
    ...
```

### MotionClient().liftRaise

[Show source in __init__.py:282](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L282)

Initiates the lifting process.

#### Signature

```python
@_ifHandleValid
def liftRaise(self):
    ...
```

### MotionClient().liftStop

[Show source in __init__.py:287](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L287)

Interrupts the lifting process.

#### Signature

```python
@_ifHandleValid
def liftStop(self):
    ...
```

### MotionClient().run

[Show source in __init__.py:308](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L308)

Activate roll and pitch rotation.
Requires start to have been executed.

#### Signature

```python
@_ifHandleValid
def run(self):
    ...
```

### MotionClient().setPitchTarget

[Show source in __init__.py:228](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L228)

Sets target pitch position in degrees.

See getPitchMax and getPitchMin for input range.

#### Signature

```python
@_ifReady
def setPitchTarget(self, val: int):
    ...
```

### MotionClient().setRollTarget

[Show source in __init__.py:202](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L202)

Sets target roll position in degrees.

See getRollMax and getRollMin for input range.

#### Signature

```python
@_ifReady
def setRollTarget(self, val: int):
    ...
```

### MotionClient().start

[Show source in __init__.py:297](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L297)

Prepares roll and pitch rotation.
Requires the lifting process be complete.

Despite the name of this function (which matches the button),
run must still be triggered to begin moving.

#### Signature

```python
@_ifHandleValid
def start(self):
    ...
```

### MotionClient().status

[Show source in __init__.py:386](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L386)

Compiles many of the status getters above into a serializable object.

This excludes any log output and min/max values as they would be redundant to save.

#### Signature

```python
@_ifHandleValid
def status(self) -> dict:
    ...
```

### MotionClient().stop

[Show source in __init__.py:321](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/__init__.py#L321)

Returns simulator to neutral rotation and halts further movement.

#### Signature

```python
@_ifHandleValid
def stop(self):
    ...
```