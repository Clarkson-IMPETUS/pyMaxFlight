try:
    import win32api
    import win32gui
    import win32process
    import win32con
    import commctrl
except:
    raise Exception("The Interface submodule requires pywin32: pip install pywin32")

import functools

# From winuser.h
MAKEWPARAM = win32api.MAKELONG

def GetListBoxCount(hwnd):
    return win32gui.SendMessage(hwnd, win32con.LB_GETCOUNT, 0, 0)

def GetListBoxLine(hwnd, lineNum):
    lineLen = win32gui.SendMessage(hwnd, win32con.LB_GETTEXTLEN, lineNum, None) * 2
    lineBuffer = win32gui.PyMakeBuffer(lineLen)
    win32gui.SendMessage(hwnd, win32con.LB_GETTEXT, lineNum, lineBuffer)
    return str(lineBuffer, 'utf8')

def GetListBoxRange(hwnd, low: int=None, high: int= None):
    if low is None:
        low = 0

    if high is None:
        high = GetListBoxCount(hwnd) - 1

    for i in range(low, high + 1):
        yield GetListBoxLine(hwnd, i)

def SetSlider(hwndDialog, hwndSlider, val: float, horizontal: bool=True):
    """
    Sets the position of a Win32 slider and triggers any listeners.
    """

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
        MAKEWPARAM(commctrl.TB_THUMBPOSITION, val),
        hwndSlider
    )

    retThumbTrack = win32gui.PostMessage(
        hwndDialog,
        msg,
        MAKEWPARAM(win32con.SB_THUMBTRACK, val),
        hwndSlider
    )

    retReleasedCapture = win32gui.PostMessage(
        hwndSlider,
        commctrl.NM_RELEASEDCAPTURE,
        0, 0
    )


class MotionClient:
    """
    Provides an interface to the MaxFlight Motion Client.
    Calling commands without the client open will result in an exception.
    NEVER use the Motion Client fully unattended.
    """

    hwndMotionClientMain = None
    _pid_cache = None

    def init(self):
        # Obtained using Spy++
        self.hwndMotionClientMain = win32gui.FindWindow(None, "MFMotion Test Client")

        if self.hwndMotionClientMain == 0:
            self._close()
            raise Exception("Motion Client not open.")

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
        return win32process.GetWindowThreadProcessId(self.hwndMotionClientMain)

    def _error(self):
        self._close()
        raise Exception("Motion Client not open.")

    def _close(self):
        self.hwndMotionClientMain = None
        self._pid_cache = None

    def ifHandleValid(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.hwndMotionClientMain is None:
                self.init()

            if not win32gui.IsWindow(self.hwndMotionClientMain):
                self._error()

            if not (self._getPID() == self._pid_cache):
                self._error()

            return func(self, *args, **kwargs)
        return wrapper

    def ifReady(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.getReady():
                raise Exception("Not ready!")

            return func(self, *args, **kwargs)
        return wrapper

    @ifHandleValid
    @ifReady
    def setRollTarget(self, val: int):
        SetSlider(self.hwndDialog, self.hwndSliderRoll, val, True)

    @ifHandleValid
    def getRollTarget(self) -> int:
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETPOS, 0, 0)

    @ifHandleValid
    def getRollMax(self) -> int:
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETRANGEMAX, 0, 0)

    @ifHandleValid
    def getRollMin(self) -> int:
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETRANGEMIN, 0, 0)

    @ifHandleValid
    @ifReady
    def setPitchTarget(self, val: int):
        SetSlider(self.hwndDialog, self.hwndSliderPitch, val, False)

    @ifHandleValid
    def getPitchTarget(self) -> int:
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETPOS, 0, 0)

    @ifHandleValid
    def getPitchMax(self) -> int:
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETRANGEMAX, 0, 0)
        
    @ifHandleValid
    def getPitchMin(self) -> int:
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETRANGEMIN, 0, 0)

    # For some reason function decorators arent working properly with this
    def _getCheckboxBool(self, hwnd) -> bool:
        return bool(win32gui.SendMessage(hwnd, win32con.BM_GETCHECK, 0, 0))

    @ifHandleValid
    def getLeftRaised(self):
        return self._getCheckboxBool(self.hwndStatusLeftRaised)

    @ifHandleValid
    def getRightRaised(self) -> bool:
        return self._getCheckboxBool(self.hwndStatusRightRaised)

    @ifHandleValid
    def getLowered(self) -> bool:
        return self._getCheckboxBool(self.hwndStatusLowered)

    @ifHandleValid
    def getEmergencyStop(self) -> bool:
        return self._getCheckboxBool(self.hwndStatusEmergencyStop)

    @ifHandleValid
    def getCanopyOpen(self) -> bool:
        return self._getCheckboxBool(self.hwndStatusCanopyOpen)

    @ifHandleValid
    def liftRaise(self):
        win32gui.SendMessage(self.hwndButtonRaise, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def liftStop(self):
        win32gui.SendMessage(self.hwndButtonLiftStop, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def liftLower(self):
        win32gui.SendMessage(self.hwndButtonLower, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def start(self):
        win32gui.SendMessage(self.hwndButtonStart, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def run(self):
        win32gui.SendMessage(self.hwndButtonRun, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def freeze(self):
        win32gui.SendMessage(self.hwndButtonFreeze, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def stop(self):
        win32gui.SendMessage(self.hwndButtonStop, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def forceRaised(self):
        win32gui.SendMessage(self.hwndButtonForceRaised, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def counterweightFwd(self):
        win32gui.SendMessage(self.hwndButtonCounterweightFwd, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def counterweightBwd(self):
        win32gui.SendMessage(self.hwndButtonCounterweightBwd, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def home(self):
        win32gui.SendMessage(self.hwndButtonHome, win32con.BM_CLICK, 0, 0)

    @ifHandleValid
    def getPitchReal(self) -> float:
        return float(win32gui.GetWindowText(self.hwndValuePitch))

    @ifHandleValid
    def getRollReal(self) -> float:
        return float(win32gui.GetWindowText(self.hwndValueRoll))

    @ifHandleValid
    def getLiftReal(self) -> float:
        return float(win32gui.GetWindowText(self.hwndValueLift))

    @ifHandleValid
    def getLogRange(self, low: int=None, high: int=None) -> list[str]:
        return GetListBoxRange(self.hwndLog, low, high)

    # =========================================================================

    @ifHandleValid
    def status(self) -> dict:
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
