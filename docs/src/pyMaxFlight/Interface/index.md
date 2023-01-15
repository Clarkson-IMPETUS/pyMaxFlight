# Interface

[Pymaxflight Index](../../../README.md#pymaxflight-index) /
`src` /
[Pymaxflight](../index.md#pymaxflight) /
Interface

> Auto-generated documentation for [src.pyMaxFlight.Interface](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py) module.

#### Attributes

- `HWND` - Typedef: `int`


## MotionClient

[Show source in __init__.py:76](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L76)

Provides an interface to the MaxFlight Motion Client.

Calling commands without the client open will result in an exception.
NEVER use the Motion Client fully unattended.

#### Signature

```python
class MotionClient:
    ...
```

### MotionClient().counterweightBwd

[Show source in __init__.py:338](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L338)

Manually moves the counterweight backwards (towards the tail).

This is for troubleshooting and is not necessary to activate under normal circumstances.

#### Signature

```python
@_ifHandleValid
def counterweightBwd(self):
    ...
```

### MotionClient().counterweightFwd

[Show source in __init__.py:329](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L329)

Manually moves the counterweight forwards (towards the cabin).

This is for troubleshooting and is not necessary to activate under normal circumstances.

#### Signature

```python
@_ifHandleValid
def counterweightFwd(self):
    ...
```

### MotionClient().forceRaised

[Show source in __init__.py:320](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L320)

Forces simulator into raised state. (?)

This is for troubleshooting and is not necessary to activate under normal circumstances.

#### Signature

```python
@_ifHandleValid
def forceRaised(self):
    ...
```

### MotionClient().freeze

[Show source in __init__.py:310](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L310)

Locks current target rotation.

#### Signature

```python
@_ifHandleValid
def freeze(self):
    ...
```

### MotionClient().getCanopyOpen

[Show source in __init__.py:266](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L266)

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

[Show source in __init__.py:261](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L261)

Gets whether the emergency stop button is pressed inwards.

#### Signature

```python
@_ifHandleValid
def getEmergencyStop(self) -> bool:
    ...
```

### MotionClient().getLeftRaised

[Show source in __init__.py:246](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L246)

Gets whether the left hydraulic lift has reached the highest position.

#### Signature

```python
@_ifHandleValid
def getLeftRaised(self):
    ...
```

### MotionClient().getLiftReal

[Show source in __init__.py:362](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L362)

Get real lift measurement. (?)

#### Signature

```python
@_ifHandleValid
def getLiftReal(self) -> float:
    ...
```

### MotionClient().getLogRange

[Show source in __init__.py:367](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L367)

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

[Show source in __init__.py:256](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L256)

Gets whether the both hydraulic lifts are at the lowest position.

#### Signature

```python
@_ifHandleValid
def getLowered(self) -> bool:
    ...
```

### MotionClient().getPitchMax

[Show source in __init__.py:236](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L236)

Gets maximum pitch position in degrees.

#### Signature

```python
@_ifHandleValid
def getPitchMax(self) -> int:
    ...
```

### MotionClient().getPitchMin

[Show source in __init__.py:241](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L241)

Gets minimum pitch position in degrees.

#### Signature

```python
@_ifHandleValid
def getPitchMin(self) -> int:
    ...
```

### MotionClient().getPitchReal

[Show source in __init__.py:352](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L352)

Get real pitch measurement.

#### Signature

```python
@_ifHandleValid
def getPitchReal(self) -> float:
    ...
```

### MotionClient().getPitchTarget

[Show source in __init__.py:231](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L231)

Gets target pitch position in degrees.

#### Signature

```python
@_ifHandleValid
def getPitchTarget(self) -> int:
    ...
```

### MotionClient().getReady

[Show source in __init__.py:190](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L190)

Returns whether simulator is ready to accept movement commands.

#### Signature

```python
@_ifHandleValid
def getReady(self) -> bool:
    ...
```

### MotionClient().getRightRaised

[Show source in __init__.py:251](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L251)

Gets whether the right hydraulic lift has reached the highest position.

#### Signature

```python
@_ifHandleValid
def getRightRaised(self) -> bool:
    ...
```

### MotionClient().getRollMax

[Show source in __init__.py:212](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L212)

Gets maximum roll position in degrees.

#### Signature

```python
@_ifHandleValid
def getRollMax(self) -> int:
    ...
```

### MotionClient().getRollMin

[Show source in __init__.py:217](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L217)

Gets minimum roll position in degrees.

#### Signature

```python
@_ifHandleValid
def getRollMin(self) -> int:
    ...
```

### MotionClient().getRollReal

[Show source in __init__.py:357](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L357)

Get real roll measurement.

#### Signature

```python
@_ifHandleValid
def getRollReal(self) -> float:
    ...
```

### MotionClient().getRollTarget

[Show source in __init__.py:207](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L207)

Gets target roll position in degrees.

#### Signature

```python
@_ifHandleValid
def getRollTarget(self) -> int:
    ...
```

### MotionClient().home

[Show source in __init__.py:347](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L347)

Sets target roll and pitch to 0.

#### Signature

```python
@_ifHandleValid
def home(self):
    ...
```

### MotionClient().liftLower

[Show source in __init__.py:286](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L286)

Initiates the lowering process.

#### Signature

```python
@_ifHandleValid
def liftLower(self):
    ...
```

### MotionClient().liftRaise

[Show source in __init__.py:276](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L276)

Initiates the lifting process.

#### Signature

```python
@_ifHandleValid
def liftRaise(self):
    ...
```

### MotionClient().liftStop

[Show source in __init__.py:281](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L281)

Interrupts the lifting process.

#### Signature

```python
@_ifHandleValid
def liftStop(self):
    ...
```

### MotionClient().run

[Show source in __init__.py:302](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L302)

Activate roll and pitch rotation.
Requires start to have been executed.

#### Signature

```python
@_ifHandleValid
def run(self):
    ...
```

### MotionClient().setPitchTarget

[Show source in __init__.py:222](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L222)

Sets target pitch position in degrees.

See getPitchMax and getPitchMin for input range.

#### Signature

```python
@_ifReady
def setPitchTarget(self, val: int):
    ...
```

### MotionClient().setRollTarget

[Show source in __init__.py:198](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L198)

Sets target roll position in degrees.

See getRollMax and getRollMin for input range.

#### Signature

```python
@_ifReady
def setRollTarget(self, val: int):
    ...
```

### MotionClient().start

[Show source in __init__.py:291](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L291)

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

[Show source in __init__.py:380](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L380)

Compiles many of the status getters above into a serializable object.

This excludes any log output and min/max values as they would be redundant to save.

#### Signature

```python
@_ifHandleValid
def status(self) -> dict:
    ...
```

### MotionClient().stop

[Show source in __init__.py:315](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Interface/__init__.py#L315)

Returns simulator to neutral rotation and halts further movement.

#### Signature

```python
@_ifHandleValid
def stop(self):
    ...
```
