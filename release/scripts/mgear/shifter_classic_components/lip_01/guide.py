"""Guide Mouth 01 module"""

import os

from maya.app.general.mayaMixin import (MayaQDockWidget,
                                        MayaQWidgetDockableMixin)
from mgear.core import pyqt, transform
from mgear.shifter.component import guide
from mgear.vendor.Qt import QtCore, QtWidgets
from mgear.shifter import io

import pymel.core as pm

# guide info
AUTHOR = "Joji Nishimura"
URL = ""
EMAIL = ""
VERSION = [1, 0, 0]
TYPE = "lip_01"
NAME = "lip"
DESCRIPTION = "Advanced lip control(Major, Minor, Corner, Pinch, Lip) as well as jaw and jaw offset control"


##########################################################
# CLASS
##########################################################


class Guide(guide.ComponentGuide):
    """Component Guide Class"""

    compType = TYPE
    compName = NAME
    description = DESCRIPTION

    author = AUTHOR
    url = URL
    email = EMAIL
    version = VERSION

    def postInit(self):
        """Initialize the position for the guide"""
        self.save_transform = [
            "root",
            "rotcenter",
            "jaw",
            "uprMajorC",
            "lwrMajorC",
            "cnrMajorL0",
            "cnrMajorR0",
            "uprMinorC",
            "lwrMinorC",
            "uprMinorL0",
            "uprMinorL1",
            "uprMinorL2",
            "uprMinorR0",
            "uprMinorR1",
            "uprMinorR2",
            "lwrMinorL0",
            "lwrMinorL1",
            "lwrMinorL2",
            "lwrMinorR0",
            "lwrMinorR1",
            "lwrMinorR2",
            "cnrMinorL0",
            "cnrMinorR0",
            "uprPinchL0",
            "uprPinchR0",
            "lwrPinchL0",
            "lwrPinchR0"
        ]

    def addObjects(self):
        """Add the Guide Root, blade and locators"""

        def addlocator(name, offset):
            """Helper function to add a locator with a given name and offset."""
            position = transform.getOffsetPosition(self.root, offset)
            return self.addLoc(name, self.root, position)

        # lip guide
        self.root = self.addRoot()

        self.rotcenter = addlocator("rotcenter", [0, 0, 1])
        self.uprMajorC = addlocator("uprMajorC", [0, 0.5, 1.5])
        self.lwrMajorC = addlocator("lwrMajorC", [0, -0.5, 1.5])
        self.cnrMinorL0 = addlocator("cnrMajorL0", [3.0, 0, 1])
        self.cnrMinorR0 = addlocator("cnrMajorR0", [-3.0, 0, 1])

        self.uprMinorC = addlocator("uprMinorC", [0, 0.5, 1])
        self.lwrMinorC = addlocator("lwrMinorC", [0, -0.5, 1])

        self.uprMinorL0 = addlocator("uprMinorL0", [0.5, 0.5, 1])
        self.uprMinorL1 = addlocator("uprMinorL1", [1.0, 0.5, 1])
        self.uprMinorL2 = addlocator("uprMinorL2", [1.5, 0.5, 1])

        self.uprMinorR0 = addlocator("uprMinorR0", [-0.5, 0.5, 1])
        self.uprMinorR1 = addlocator("uprMinorR1", [-1.0, 0.5, 1])
        self.uprMinorR2 = addlocator("uprMinorR2", [-1.5, 0.5, 1])

        self.lwrMinorL0 = addlocator("lwrMinorL0", [0.5, -0.5, 1])
        self.lwrMinorL1 = addlocator("lwrMinorL1", [1.0, -0.5, 1])
        self.lwrMinorL2 = addlocator("lwrMinorL2", [1.5, -0.5, 1])

        self.lwrMinorR0 = addlocator("lwrMinorR0", [-0.5, -0.5, 1])
        self.lwrMinorR1 = addlocator("lwrMinorR1", [-1.0, -0.5, 1])
        self.lwrMinorR2 = addlocator("lwrMinorR2", [-1.5, -0.5, 1])

        self.cnrMinorL0 = addlocator("cnrMinorL0", [2.5, 0, 1])
        self.cnrMinorR0 = addlocator("cnrMinorR0", [-2.5, 0, 1])

        self.uprPinchL0 = addlocator("uprPinchL0", [2.3, 0.5, 1])
        self.lwrPinchL0 = addlocator("lwrPinchL0", [2.3, -0.5, 1])

        self.uprPinchR0 = addlocator("uprPinchR0", [-2.3, 0.5, 1])
        self.lwrPinchR0 = addlocator("lwrPinchR0", [-2.3, -0.5, 1])

        # jaw
        self.jaw = addlocator("jaw", [0, -1.3, 1.3])

        centers = [self.root, self.rotcenter]
        self.dispcrv = self.addDispCurve("crv", centers)

        centers = [self.root, self.jaw]
        self.dispcrv = self.addDispCurve("crv", centers)

    def addParameters(self):
        """Add the configurations settings"""

        self.pUseIndex = self.addParam("useIndex", "bool", False)
        self.pParentJointIndex = self.addParam(
            "parentJointIndex", "long", -1, None, None)

        return


##########################################################
# Setting Page
##########################################################


class componentSettings(MayaQWidgetDockableMixin, guide.componentMainSettings):
    """Create the component setting window"""

    def __init__(self, parent=None):
        self.toolName = TYPE
        # Delete old instances of the componet settings window.
        pyqt.deleteInstances(self, MayaQDockWidget)

        super(self.__class__, self).__init__(parent=parent)

        self.setup_componentSettingWindow()
        self.create_componentControls()
        self.populate_componentControls()
        self.create_componentLayout()
        self.create_componentConnections()

    def setup_componentSettingWindow(self):
        self.mayaMainWindow = pyqt.maya_main_window()

        self.setObjectName(self.toolName)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle(TYPE)
        self.resize(280, 350)

    def create_componentControls(self):
        return

    def populate_componentControls(self):
        """Populate the controls values.

        Populate the controls values from the custom attributes of the
        component.

        """
        return

    def create_componentLayout(self):
        self.settings_layout = QtWidgets.QVBoxLayout()
        self.settings_layout.addWidget(self.tabs)
        self.settings_layout.addWidget(self.close_button)

        self.setLayout(self.settings_layout)

    def create_componentConnections(self):
        return

    def dockCloseEventTriggered(self):
        pyqt.deleteInstances(self, MayaQDockWidget)
