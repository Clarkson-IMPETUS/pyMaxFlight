import win32api
import win32gui
import win32process
import win32con
import commctrl
import ctypes

import functools
from typing import Iterator

# Typedef
HWND = int

def _GetCheckboxBool(hwnd: HWND) -> bool:
    """Gets the status a Win32 Checkbox as a bool. (Checked is True.)"""
    return bool(win32gui.SendMessage(hwnd, win32con.BM_GETCHECK, 0, 0))

def _GetListBoxCount(hwnd: HWND) -> int:
    """Gets number of items in a Win32 ListBox."""
    return win32gui.SendMessage(hwnd, win32con.LB_GETCOUNT, 0, 0)

def _GetListBoxLine(hwnd: HWND, lineNum: int) -> str:
    """Gets line by index in a Win32 ListBox."""
    lineLen = win32gui.SendMessage(hwnd, win32con.LB_GETTEXTLEN, lineNum, None) * 2
    lineBuffer = win32gui.PyMakeBuffer(lineLen)
    win32gui.SendMessage(hwnd, win32con.LB_GETTEXT, lineNum, lineBuffer)
    return str(lineBuffer, 'utf8')

def _GetListBoxRange(hwnd: HWND, low: int=0, high: int= None) -> Iterator[str]:
    """Gets range of lines by index (inclusive) in a Win32 ListBox."""

    if low is None:
        low = 0

    if high is None:
        high = _GetListBoxCount(hwnd) - 1

    for i in range(low, high + 1):
        yield _GetListBoxLine(hwnd, i)

def _SetSlider(hwndDialog: HWND, hwndSlider: HWND, val: float, horizontal: bool=True):
    """Sets the position of a Win32 slider and triggers any listeners."""

    retSetPos = win32gui.PostMessage(
        hwndSlider,
        commctrl.TBM_SETPOS,
        True, # Redraw
        val
    )

    msg = win32con.WM_HSCROLL if horizontal else win32con.WM_VSCROLL
    
    retThumbPos = win32gui.PostMessage(
        hwndDialog,
        msg,
        win32api.MAKELONG(commctrl.TB_THUMBPOSITION, val),
        hwndSlider
    )

    retThumbTrack = win32gui.PostMessage(
        hwndDialog,
        msg,
        win32api.MAKELONG(win32con.SB_THUMBTRACK, val),
        hwndSlider
    )

    # For some reason doing this with win32gui was giving errors
    # Doesn't require another external library so ¯\_(ツ)_/¯
    retReleasedCapture = ctypes.windll.user32.PostMessageA(
        hwndSlider,
        commctrl.NM_RELEASEDCAPTURE,
        None,
        None
    )


class MotionClient:
    """
    Provides an interface to the MaxFlight Motion Client.
    
    Calling commands without the client open will result in an exception.
    NEVER use the Motion Client fully unattended.
    """

    hwndMotionClientMain = None
    _pid_cache = None

    def _init(self):
        """
        Obtains handles to Motion Client.

        This is called automatically when using any public functions.
        This should not be called manually. If this results in latency issues,
        you may need to refactor this to be public.

        Raises an Exception if Motion Client not open.
        """
        # Obtained using Spy++
        self.hwndMotionClientMain = win32gui.FindWindow(None, "MFMotion Test Client")

        if self.hwndMotionClientMain == 0:
            self._error()

        self._pid_cache = self._getPID()

        hwndMDIClient   = win32gui.FindWindowEx(self.hwndMotionClientMain, None, "MDIClient", None)

        if hwndMDIClient == 0:
            self._error()

        hwndMotionView1 = win32gui.FindWindowEx(hwndMDIClient, None, None, "MotionView1")

        if hwndMotionView1 == 0:
            self._error()

        self.hwndDialog      = win32gui.FindWindowEx(hwndMotionView1, None, None, "")

        if self.hwndDialog == 0:
            self._error()

        self.hwndButtonRaise            = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Raise")
        self.hwndButtonLiftStop         = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Stop")
        self.hwndButtonLower            = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Lower")
        self.hwndButtonStart            = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Start")
        self.hwndButtonRun              = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Run")
        self.hwndButtonFreeze           = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Freeze")
        self.hwndButtonStop             = win32gui.FindWindowEx(self.hwndDialog, self.hwndButtonFreeze, "Button", "Stop")
        self.hwndButtonForceRaised      = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Force Raised")
        self.hwndButtonCounterweightFwd = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "FORWARD")
        self.hwndButtonCounterweightBwd = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "BACK")
        self.hwndButtonHome             = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "--|--")
        self.hwndSliderRoll             = win32gui.FindWindowEx(self.hwndDialog, 0, "msctls_trackbar32", "Slider1")
        self.hwndSliderPitch            = win32gui.FindWindowEx(self.hwndDialog, 0, "msctls_trackbar32", "Slider2")
        self.hwndStatusLeftRaised       = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Left Raised")
        self.hwndStatusRightRaised      = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Right Raised")
        self.hwndStatusLowered          = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Lowered")
        self.hwndStatusEmergencyStop    = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Emergency Stop")
        self.hwndStatusCanopyOpen       = win32gui.FindWindowEx(self.hwndDialog, 0, "Button", "Canopy Open")
        
        self.hwndLog                    = win32gui.FindWindowEx(self.hwndDialog, 0, "ListBox", None)

        hwndCaptionLift                 = win32gui.FindWindowEx(self.hwndDialog, 0, "Static", "Lift")
        self.hwndValuePitch             = win32gui.FindWindowEx(self.hwndDialog, hwndCaptionLift, "Static", None)
        self.hwndValueRoll              = win32gui.FindWindowEx(self.hwndDialog, self.hwndValuePitch, "Static", None)
        self.hwndValueLift              = win32gui.FindWindowEx(self.hwndDialog, self.hwndValueRoll, "Static", None)

    def _getPID(self):
        """Gets process ID of Motion Client."""
        return win32process.GetWindowThreadProcessId(self.hwndMotionClientMain)

    def _error(self):
        """Performs cleanup and raises and Exception."""
        self._close()
        raise Exception("Motion Client not open.")

    def _close(self):
        """Cleans up existing handles and cache."""
        self.hwndMotionClientMain = None
        self._pid_cache = None

    @property
    def isMotionClientOpen(self) -> bool:
        """True if Motion Client is open, otherwise False."""
        if self.hwndMotionClientMain is None:
            self._init()

        if not win32gui.IsWindow(self.hwndMotionClientMain):
            return False

        if not (self._getPID() == self._pid_cache):
            return False
        
        return True

    def _ifHandleValid(func):
        """Function decorator that prevents propagation if the current window handle is invalid."""
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.isMotionClientOpen:
                self._error()

            return func(self, *args, **kwargs)
        return wrapper

    def _ifReady(func):
        """
        Function decorator that prevents propagation if the simulator is not ready.
        
        See getReady for readiness criteria.
        """
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.getReady():
                raise Exception("Not ready!")

            return func(self, *args, **kwargs)
        return wrapper

    @_ifHandleValid
    def getReady(self) -> bool:
        """Returns whether simulator is ready to accept movement commands."""
        return (
            (not self.getEmergencyStop()) and
            (not self.getCanopyOpen())
        )

    @_ifHandleValid
    def setRollTarget(self, val: int):
        """
        Sets target roll position in degrees.
        
        See getRollMax and getRollMin for input range.
        """
        _SetSlider(self.hwndDialog, self.hwndSliderRoll, val, True)

    @_ifHandleValid
    def getRollTarget(self) -> int:
        """Gets target roll position in degrees."""
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETPOS, 0, 0)

    @_ifHandleValid
    def getRollMax(self) -> int:
        """Gets maximum roll position in degrees."""
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETRANGEMAX, 0, 0)

    @_ifHandleValid
    def getRollMin(self) -> int:
        """Gets minimum roll position in degrees."""
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETRANGEMIN, 0, 0)

    # For some reason the display value in MotionClient and the slider position
    # are negative to each other. To match that, we negate it here too
    @_ifHandleValid
    def setPitchTarget(self, val: int):
        """
        Sets target pitch position in degrees.
        
        See getPitchMax and getPitchMin for input range.
        """
        _SetSlider(self.hwndDialog, self.hwndSliderPitch, -val, False)

    @_ifHandleValid
    def getPitchTarget(self) -> int:
        """Gets target pitch position in degrees."""
        return -win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETPOS, 0, 0)

    @_ifHandleValid
    def getPitchMax(self) -> int:
        """Gets maximum pitch position in degrees."""
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETRANGEMAX, 0, 0)
        
    @_ifHandleValid
    def getPitchMin(self) -> int:
        """Gets minimum pitch position in degrees."""
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETRANGEMIN, 0, 0)

    @_ifHandleValid
    def getLeftRaised(self):
        """Gets whether the left hydraulic lift has reached the highest position."""
        return _GetCheckboxBool(self.hwndStatusLeftRaised)

    @_ifHandleValid
    def getRightRaised(self) -> bool:
        """Gets whether the right hydraulic lift has reached the highest position."""
        return _GetCheckboxBool(self.hwndStatusRightRaised)

    @_ifHandleValid
    def getLowered(self) -> bool:
        """Gets whether the both hydraulic lifts are at the lowest position."""
        return _GetCheckboxBool(self.hwndStatusLowered)

    @_ifHandleValid
    def getEmergencyStop(self) -> bool:
        """Gets whether the emergency stop button is pressed inwards."""
        return _GetCheckboxBool(self.hwndStatusEmergencyStop)

    @_ifHandleValid
    def getCanopyOpen(self) -> bool:
        """
        Gets whether the canopy is open.
        
        Note that this does not indicate whether the canopy is locked.
        There is currently no way to detect this.
        """
        return _GetCheckboxBool(self.hwndStatusCanopyOpen)

    @_ifHandleValid
    def liftRaise(self):
        """Initiates the lifting process."""
        win32gui.SendMessage(self.hwndButtonRaise, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def liftStop(self):
        """Interrupts the lifting process."""
        win32gui.SendMessage(self.hwndButtonLiftStop, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def liftLower(self):
        """Initiates the lowering process."""
        win32gui.SendMessage(self.hwndButtonLower, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def start(self):
        """
        Prepares roll and pitch rotation.
        Requires the lifting process be complete.
        
        Despite the name of this function (which matches the button),
        run must still be triggered to begin moving.
        """
        win32gui.SendMessage(self.hwndButtonStart, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def run(self):
        """
        Activate roll and pitch rotation.
        Requires start to have been executed.
        """
        win32gui.SendMessage(self.hwndButtonRun, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def freeze(self):
        """Locks current target rotation."""
        win32gui.SendMessage(self.hwndButtonFreeze, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def stop(self):
        """Returns simulator to neutral rotation and halts further movement."""
        win32gui.SendMessage(self.hwndButtonStop, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def forceRaised(self):
        """
        Forces simulator into raised state. (?)

        This is for troubleshooting and is not necessary to activate under normal circumstances.
        """
        win32gui.SendMessage(self.hwndButtonForceRaised, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def counterweightFwd(self):
        """
        Manually moves the counterweight forwards (towards the cabin).

        This is for troubleshooting and is not necessary to activate under normal circumstances.
        """
        win32gui.SendMessage(self.hwndButtonCounterweightFwd, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def counterweightBwd(self):
        """
        Manually moves the counterweight backwards (towards the tail).

        This is for troubleshooting and is not necessary to activate under normal circumstances.
        """
        win32gui.SendMessage(self.hwndButtonCounterweightBwd, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def home(self):
        """Sets target roll and pitch to 0."""
        win32gui.SendMessage(self.hwndButtonHome, win32con.BM_CLICK, 0, 0)

    @_ifHandleValid
    def getPitchReal(self) -> float:
        """Get real pitch measurement."""
        return float(win32gui.GetWindowText(self.hwndValuePitch))

    @_ifHandleValid
    def getRollReal(self) -> float:
        """Get real roll measurement."""
        return float(win32gui.GetWindowText(self.hwndValueRoll))

    @_ifHandleValid
    def getLiftReal(self) -> float:
        """Get real lift measurement. (?)"""
        return float(win32gui.GetWindowText(self.hwndValueLift))

    @_ifHandleValid
    def getLogRange(self, low: int=0, high: int=None) -> list[str]:
        """
        Gets range of log messages.
        
        If low is undefined, it will be set to 0.
        If high is undefined, it will be set to the last element of the list.
        Both indices are inclusive.
        """
        return _GetListBoxRange(self.hwndLog, low, high)

    # =========================================================================

    @_ifHandleValid
    def status(self) -> dict:
        """
        Compiles many of the status getters above into a serializable object.

        This excludes any log output and min/max values as they would be redundant to save.
        """
        return {
            "canopyOpen": self.getCanopyOpen(),
            "emergencyStop": self.getEmergencyStop(),
            "lowered": self.getLowered(),
            "raised": {
                "left": self.getLeftRaised(),
                "right": self.getRightRaised(),
            },
            "pitch": {
                "real": self.getPitchReal(),
                "target": self.getPitchTarget(),
                # "min": self.getPitchMin(),
                # "max": self.getPitchMax()
            },
            "roll": {
                "real": self.getRollReal(),
                "target": self.getRollTarget(),
                # "min": self.getRollMin(),
                # "max": self.getRollMax()
            },
            "lift": self.getLiftReal()
        }
