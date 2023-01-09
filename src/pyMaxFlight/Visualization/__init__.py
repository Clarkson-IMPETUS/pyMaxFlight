import os

from panda3d.core import Filename, NodePath, loadPrcFileData, AntialiasAttrib
from direct.showbase.ShowBase import ShowBase
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from .. import Processing

def swizzleTuple(a, newOrder):
    return (
        a[newOrder[0]],
        a[newOrder[1]],
        a[newOrder[2]]
    )

def setFigSizePx(fig, w, h, dpi=96):
    dpi = float(dpi)
    fig.set_dpi(dpi)
    fig.set_size_inches(w/dpi, h/dpi)

class Plot2D:
    def __init__(
        self,
        data,
        axis = "roll",
        other = []
    ):
        self._data = data
        self._axis = axis

        self._vline = None
        self._hline = None

        self._timeStart, self._timesRelative = Processing.getRelativeTimes(data)

        self.fig, self._ax = plt.subplots()

        self._ax.set_title("Target vs. Real " + axis.capitalize())
        self._ax.set_xlabel(f"Unix Timestamp (Seconds, +{self._timeStart})")
        self._ax.set_ylabel("Angle (Degrees)")

        self._ax.plot(
            self._timesRelative,
            data[axis + "_real"],
            label="Real"
        )
        self._ax.plot(
            self._timesRelative,
            data[axis + "_target"],
            label="Target"
        )

        for item in other:
            y = item[0]
            label = item[1]
            self._ax.plot(self._timesRelative, y, label=label)

        self._ax.legend(loc="upper left")

        self._ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(base=90.0))
        self._ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(base=2))

        setFigSizePx(self.fig, 512, 256, 96)
        self.fig.tight_layout(pad=0)
        self.fig.subplots_adjust(left=0.14, right=0.99, top=0.9, bottom=0.175)

        self.update(self._timeStart)

    def update(
        self,
        timeCurrent
    ):
        timeCurrentRelative = timeCurrent - self._timeStart
        yCurrentVal = Processing.getValueAtTime(self._data, timeCurrent, self._axis)

        if not (self._vline is None):
            self._vline.remove()
        self._vline = self._ax.axvline(x = timeCurrentRelative, color='k', alpha=0.25)

        if not (self._hline is None):
            self._hline.remove()
        self._hline = self._ax.axhline(y = yCurrentVal, color='k', alpha=0.25)

        xrange = 15
        yrange = 360

        self._ax.set_xlim(timeCurrentRelative - xrange, timeCurrentRelative + xrange)
        self._ax.set_ylim(yCurrentVal - yrange, yCurrentVal + yrange)


class Visualizer3D:
    def __init__(self, resolution=(256, 256)):
        loadPrcFileData("", f"win-size {resolution[0]} {resolution[1]}")
        
        self.base = ShowBase( windowType='offscreen')
        self.base.render.setAntialias(AntialiasAttrib.MAuto)

        centeredCube = NodePath('centeredCube')
        cubeModelPath = Filename.fromOsSpecific(
            os.path.join(
                os.path.dirname(__file__),
                "models",
                 'coloredCube.glb'
            )
        )

        cube = self.base.loader.loadModel(cubeModelPath)
        cube.reparentTo(centeredCube)

        swizzleOrder = (2, 0, 1)

        root = self.base.render.attachNewNode('root')

        self.pitch = root.attachNewNode('pitch')

        pitchCube = centeredCube.copyTo(self.pitch)
        pitchCube.setScale(swizzleTuple((3, 2, 7.3), swizzleOrder))
        pitchCube.setPos(swizzleTuple((0, 0, -2.15), swizzleOrder))

        pitchArm = centeredCube.copyTo(self.pitch)
        pitchArm.setScale(swizzleTuple((6, 0.25, 0.25), swizzleOrder))

        self.roll = self.pitch.attachNewNode('roll')
        self.roll.setPos(swizzleTuple((0, 0, 1.5), swizzleOrder))

        rollCube = centeredCube.copyTo(self.roll)
        rollCube.setScale(swizzleTuple((4.3, 4.3, 4), swizzleOrder))
        rollCube.setPos(swizzleTuple((0, 0, 2), swizzleOrder))

    def getRoll(self):
        return self.roll.getP()

    def setRoll(self, angle):
        self.roll.setP(angle)

    def getPitch(self):
        return self.pitch.getR()

    def setPitch(self, angle):
        self.pitch.setR(angle)

    def render(self):
        """
        Outputs an RGBA image.
        You'll likely want to remove the alpha channel.
        """

        dist = 15
        self.base.camera.setPos(dist,-dist,dist)
        self.base.camera.lookAt(0,0,0)

        self.base.graphicsEngine.renderFrame()
        dr = self.base.camNode.getDisplayRegion(0)
        tex = dr.getScreenshot()
        data = tex.getRamImage()
        v = memoryview(data).tolist()
        img = np.array(v,dtype=np.uint8)
        img = img.reshape((tex.getYSize(),tex.getXSize(),4))
        return img[::-1]