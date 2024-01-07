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
        self.save_transform = ["root", "rotcenter", "jaw"]

    def addObjects(self):
        """Add the Guide Root, blade and locators"""

        # lip guide
        self.root = self.addRoot()
        vTemp = transform.getOffsetPosition(self.root, [0, 0, 1])
        self.rotcenter = self.addLoc("rotcenter", self.root, vTemp)

        # jaw
        vTemp = transform.getOffsetPosition(self.root, [0, -1.3, 1.3])
        self.jaw = self.addLoc("jaw", self.root, vTemp)

        centers = [self.root, self.rotcenter]
        self.dispcrv = self.addDispCurve("crv", centers)

        centers = [self.root, self.jaw]
        self.dispcrv = self.addDispCurve("crv", centers)


        moduleDir = os.path.dirname(__file__)
        io.import_guide_template(os.path.join(moduleDir, "lips.sgt"), initParent=self.root)


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
