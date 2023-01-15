# Visualization

[Pymaxflight Index](../../../README.md#pymaxflight-index) /
`src` /
[Pymaxflight](../index.md#pymaxflight) /
Visualization

> Auto-generated documentation for [src.pyMaxFlight.Visualization](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py) module.

## Plot2D

[Show source in __init__.py:23](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L23)

#### Signature

```python
class Plot2D:
    def __init__(self, data, axis="roll", other=[]):
        ...
```

### Plot2D().update

[Show source in __init__.py:71](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L71)

#### Signature

```python
def update(self, timeCurrent):
    ...
```



## Visualizer3D

[Show source in __init__.py:93](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L93)

#### Signature

```python
class Visualizer3D:
    def __init__(self, resolution=(256, 256)):
        ...
```

### Visualizer3D().getPitch

[Show source in __init__.py:138](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L138)

#### Signature

```python
def getPitch(self):
    ...
```

### Visualizer3D().getRoll

[Show source in __init__.py:132](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L132)

#### Signature

```python
def getRoll(self):
    ...
```

### Visualizer3D().render

[Show source in __init__.py:144](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L144)

Outputs an RGBA image.
You'll likely want to remove the alpha channel.

#### Signature

```python
def render(self):
    ...
```

### Visualizer3D().setPitch

[Show source in __init__.py:141](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L141)

#### Signature

```python
def setPitch(self, angle):
    ...
```

### Visualizer3D().setRoll

[Show source in __init__.py:135](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L135)

#### Signature

```python
def setRoll(self, angle):
    ...
```



## setFigSizePx

[Show source in __init__.py:18](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L18)

#### Signature

```python
def setFigSizePx(fig, w, h, dpi=96):
    ...
```



## swizzleTuple

[Show source in __init__.py:11](https://github.com/Clarkson-IMPETUS/pyMaxFlight/blob/main/src/pyMaxFlight/Visualization/__init__.py#L11)

#### Signature

```python
def swizzleTuple(a, newOrder):
    ...
```
