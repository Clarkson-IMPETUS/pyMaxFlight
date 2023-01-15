# Processing

[Pymaxflight Index](../../../README.md#pymaxflight-index) /
`src` /
[Pymaxflight](../index.md#pymaxflight) /
Processing

> Auto-generated documentation for [src.pyMaxFlight.Processing](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py) module.

## getModuloOffset

[Show source in __init__.py:34](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L34)

#### Signature

```python
def getModuloOffset(obj: list or pd.DataFrame, key: str = None) -> float:
    ...
```



## getRelativeTimes

[Show source in __init__.py:10](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L10)

#### Signature

```python
def getRelativeTimes(data):
    ...
```



## getTimeIndex

[Show source in __init__.py:20](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L20)

#### Signature

```python
def getTimeIndex(data, timeCurrent):
    ...
```



## getValueAtIndex

[Show source in __init__.py:23](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L23)

#### Signature

```python
def getValueAtIndex(data, index, axis="roll", realOrTarget="real"):
    ...
```



## getValueAtTime

[Show source in __init__.py:26](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L26)

#### Signature

```python
def getValueAtTime(data, timeCurrent, axis="roll", realOrTarget="real"):
    ...
```



## loadData

[Show source in __init__.py:4](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L4)

#### Signature

```python
def loadData(csvPath):
    ...
```



## modulateStartAndOffset

[Show source in __init__.py:53](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L53)

Determines angular modulation from the first value in the data.
(eg. If the first value was 400, it would be modulated to 40.)
This offset is then applied to all data.

This modifies `obj` in place.
If this isn't desired, copy it manually first.

#### Signature

```python
def modulateStartAndOffset(obj: list or pd.DataFrame, key: str = None) -> None:
    ...
```



## removeModulation

[Show source in __init__.py:72](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Processing/__init__.py#L72)

Removes angular modulation (in degrees) from data. Accepts both
standard lists and Pandas dataframes (using a key to a column).

This modifies `obj` in place.
If this isn't desired, copy it manually first.

#### Signature

```python
def removeModulation(obj: list or pd.DataFrame, key: str = None) -> None:
    ...
```
