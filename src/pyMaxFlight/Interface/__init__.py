try:
    import win32api
    import win32gui
    import commctrl
except:
    raise Exception("The Interface submodule requires pywin32: pip install pywin32")

# From winuser.h
WM_HSCROLL = 0x0114
WM_VSCROLL = 0x0115
SB_THUMBTRACK = 5
MAKEWPARAM = win32api.MAKELONG

# From commctrl.h
NM_FIRST = 0
NM_RELEASEDCAPTURE = (NM_FIRST-16)
BM_GETCHECK = 0x00F0

def SetSlider(hwndDialog, hwndSlider, val, horizontal=True):
    """
    Sets the position of a Win32 slider and triggers any listeners.
    """

    retSetPos = win32gui.PostMessage(
        hwndSlider,
        commctrl.TBM_SETPOS,
        True, # Redraw
        val
    )

    msg = WM_HSCROLL if horizontal else WM_VSCROLL
    
    retThumbPos = win32gui.PostMessage(
        hwndDialog,
        msg,
        MAKEWPARAM(commctrl.TB_THUMBPOSITION, val),
        hwndSlider
    )

    retThumbTrack = win32gui.PostMessage(
        hwndDialog,
        msg,
        MAKEWPARAM(SB_THUMBTRACK, val),
        hwndSlider
    )

    retReleasedCapture = win32gui.PostMessage(
        hwndSlider,
        NM_RELEASEDCAPTURE,
        0, 0
    )


class MotionClient:
    """
    Provides an interface to the MaxFlight Motion Client.
    This assumes the Motion Client is already open.
    NEVER use the Motion Client fully unattended.
    """

    def __init__(self):
        # Obtained using Spy++
        hwndMotionClientMain = win32gui.FindWindow(None, "MFMotion Test Client")

        if hwndMotionClientMain == 0:
            raise Exception("Motion Client not open.")

        hwndMDIClient   = win32gui.FindWindowEx(hwndMotionClientMain, None, "MDIClient", None)
        hwndMotionView1 = win32gui.FindWindowEx(hwndMDIClient, None, None, "MotionView1")
        self.hwndDialog      = win32gui.FindWindowEx(hwndMotionView1, None, None, "")

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
        
        hwndCaptionLift                 = win32gui.FindWindowEx(self.hwndDialog, 0, "Static", "Lift")
        self.hwndValuePitch             = win32gui.FindWindowEx(self.hwndDialog, hwndCaptionLift, "Static", None)
        self.hwndValueRoll              = win32gui.FindWindowEx(self.hwndDialog, self.hwndValuePitch, "Static", None)
        self.hwndValueLift              = win32gui.FindWindowEx(self.hwndDialog, self.hwndValueRoll, "Static", None)

    def setRollTarget(self, val):
        if not self.getReady():
            return
        SetSlider(self.hwndDialog, self.hwndSliderRoll, val, True)

    def getRollTarget(self):
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETPOS, 0, 0)

    def getRollMax(self):
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETRANGEMAX, 0, 0)

    def getRollMin(self):
        return win32gui.SendMessage(self.hwndSliderRoll, commctrl.TBM_GETRANGEMIN, 0, 0)

    def setPitchTarget(self, val):
        if not self.getReady():
            return
        SetSlider(self.hwndDialog, self.hwndSliderPitch, val, False)

    def getPitchTarget(self):
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETPOS, 0, 0)

    def getPitchMax(self):
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETRANGEMAX, 0, 0)
        
    def getPitchMin(self):
        return win32gui.SendMessage(self.hwndSliderPitch, commctrl.TBM_GETRANGEMIN, 0, 0)

    def getLeftRaised(self):
        return win32gui.SendMessage(self.hwndStatusLeftRaised, BM_GETCHECK, 0, 0) # TODO: CHECK THIS

    def getRightRaised(self):
        return win32gui.SendMessage(self.hwndStatusRightRaised, BM_GETCHECK, 0, 0) # TODO: CHECK THIS

    def getLowered(self):
        return win32gui.SendMessage(self.hwndStatusLowered, BM_GETCHECK, 0, 0) # TODO: CHECK THIS

    def getEmergencyStop(self):
        return win32gui.SendMessage(self.hwndStatusEmergencyStop, BM_GETCHECK, 0, 0) # TODO: CHECK THIS

    def getCanopyOpen(self):
        return win32gui.SendMessage(self.hwndStatusCanopyOpen, BM_GETCHECK, 0, 0) # TODO: CHECK THIS

    # TODO: Fix this
    def getReady(self):
        return True
        return (
            (not self.getLowered()) and
            (not self.getEmergencyStop()) and
            (not self.getCanopyOpen()) and
            self.getLeftRaised() and
            self.getRightRaised()
        )

    def startRaise(self):
        win32gui.SendMessage(self.hwndButtonRaise, commctrl.BM_CLICK, 0, 0)

    def liftStop(self):
        win32gui.SendMessage(self.hwndButtonLiftStop, commctrl.BM_CLICK, 0, 0)

    def lower(self):
        win32gui.SendMessage(self.hwndButtonLower, commctrl.BM_CLICK, 0, 0)

    def start(self):
        win32gui.SendMessage(self.hwndButtonStart, commctrl.BM_CLICK, 0, 0)

    def run(self):
        win32gui.SendMessage(self.hwndButtonRun, commctrl.BM_CLICK, 0, 0)

    def freeze(self):
        win32gui.SendMessage(self.hwndButtonFreeze, commctrl.BM_CLICK, 0, 0)

    def stop(self):
        win32gui.SendMessage(self.hwndButtonStop, commctrl.BM_CLICK, 0, 0)

    def forceRaised(self):
        win32gui.SendMessage(self.hwndButtonForceRaised, commctrl.BM_CLICK, 0, 0)

    def counterweightFwd(self):
        win32gui.SendMessage(self.hwndButtonCounterweightFwd, commctrl.BM_CLICK, 0, 0)

    def counterweightBwd(self):
        win32gui.SendMessage(self.hwndButtonCounterweightBwd, commctrl.BM_CLICK, 0, 0)

    def home(self):
        win32gui.SendMessage(self.hwndButtonHome, commctrl.BM_CLICK, 0, 0)

    def getPitchReal(self):
        return float(win32gui.GetWindowText(self.hwndValuePitch))

    def getRollReal(self):
        return float(win32gui.GetWindowText(self.hwndValueRoll))

    def getLiftReal(self):
        return float(win32gui.GetWindowText(self.hwndValueLift))

    def getOrientation(self):
        return (
            self.getPitchReal(),
            self.getRollReal()
        )