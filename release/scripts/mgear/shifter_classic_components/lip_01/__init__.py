"""Component Mouth 01 module"""

import pymel.core as pm
from mgear.core import attribute, primitive, transform
from mgear.shifter import component
from pymel.core import datatypes


#############################################
# COMPONENT
#############################################


class Component(component.Main):
    """Shifter component Class"""

    # =====================================================
    # OBJECTS
    # =====================================================
    def addObjects(self):
        """Add all the objects needed to create the component."""

        t = transform.getTransformFromPos(self.guide.pos["root"])
        self.ctlNpo = primitive.addTransform(
            self.root, self.getName("control_npo"), t)

        # mouth center
        t = transform.getTransformFromPos(self.guide.pos["rotcenter"])
        self.mouthCenter_npo = primitive.addTransform(
            self.ctlNpo, self.getName("mouthCenter_npo"), t)
        self.mouthCenter = primitive.addTransform(
            self.mouthCenter_npo, self.getName("mouthCenter"), t)

        # self.createJawCtrl()
        self.createLipCtrl()
        self.createNodesSDK()

        # self.createJnt()

    def createJawCtrl(self):
        pass
        # # jaw control
        # t = transform.getTransformFromPos(self.guide.pos["jaw"])
        # self.ctl_npo = primitive.addTransform(
        #     self.ctlNpo, self.getName("jaw_npo"), t)
        #
        # self.jaw_ctl = self.addCtl(
        #     self.ctl_npo,
        #     "jaw_ctl",
        #     t,
        #     self.color_fk,
        #     "circle",
        #     w=0.5 * self.size,
        #     ro=datatypes.Vector([1.5708, 0, 0]),
        #     tp=self.parentCtlTag)
        #
        # attribute.setKeyableAttributes(self.jaw_ctl, ["tx", "ty", "tz", "rz"])
        #
        # # jaw "UPPER"
        # t = transform.getTransformFromPos(self.guide.pos["root"])
        # self.jawUp_npo = primitive.addTransform(
        #     self.mouthCenter, self.getName("jawUpper_npo"), t)
        # self.jawUp_pos = primitive.addTransform(
        #     self.jawUp_npo, self.getName("jawUpper_pos"), t)
        # self.jawUp_rot = primitive.addTransform(
        #     self.jawUp_pos, self.getName("jawUpper_rot"), t)
        #
        # # jaw "LOWER"
        # t = transform.getTransformFromPos(self.guide.pos["root"])
        # self.jawLow_npo = primitive.addTransform(
        #     self.mouthCenter, self.getName("jaw_npo"), t)
        # self.jawLow_pos = primitive.addTransform(
        #     self.jawLow_npo, self.getName("jawLow_pos"), t)
        # self.jawLow_rot = primitive.addTransform(
        #     self.jawLow_pos, self.getName("jawLow_rot"), t)
        #
        # self.jawOfsset_ctl = self.addCtl(
        #     self.jawLow_rot,
        #     "jawOffset_ctl",
        #     t,
        #     self.color_fk,
        #     "circle",
        #     w=0.5 * self.size,
        #     tp=self.jaw_ctl)

    def createLipCtrl(self):
        def createControl(name, position_key, parent, color, shape, width, rotation=None):
            """Helper function to create a control with given specifications."""
            t = transform.getTransformFromPos(self.guide.pos[position_key])
            npo = primitive.addTransform(parent, self.getName(name + "_npo"), t)

            if rotation is None:
                rotation = datatypes.Vector([0, 0, 0])

            ctrl = self.addCtl(
                npo,
                name,
                t,
                color,
                shape,
                w=width * self.size,
                ro=rotation,
                tp=self.parentCtlTag
            )

            return npo, ctrl

        t = transform.getTransformFromPos(self.guide.pos["root"])

        # Major Control
        npo = primitive.addTransform(self.ctlNpo, self.getName("major_npo"), t)
        self.uprMajorC0Npo, self.uprMajorC0Ctrl = createControl(
            "uprMajorC", "uprMajorC", npo, 17, "circle", 0.1)
        self.lwrMajorC0Npo, self.lwrMajorC0Ctrl = createControl(
            "lwrMajorC", "lwrMajorC", npo, 17, "circle", 0.1)
        self.cnrMajorL0Npo, self.cnrMajorL0Ctrl = createControl(
            "cnrMajorL0", "cnrMajorL0", npo, 18, "circle", 0.1)
        self.cnrMajorR0Npo, self.cnrMajorR0Ctrl = createControl(
            "cnrMajorR0", "cnrMajorR0", npo, 20, "circle", 0.1)

        # Minor Control
        npo = primitive.addTransform(self.ctlNpo, self.getName("minor_npo"), t)
        self.uprMinorC0Npo, self.uprMinorC0Ctrl = createControl(
            "uprMinorC", "uprMinorC", npo, 17, "circle", 0.1)
        self.lwrMinorC0Npo, self.lwrMinorC0Ctrl = createControl(
            "lwrMinorC", "lwrMinorC", npo, 17, "circle", 0.1)

        self.cnrMinorL0Npo, self.cnrMinorL0Ctrl = createControl(
            "cnrMinorL0", "cnrMinorL0", npo, 18, "circle", 0.1)
        self.uprMinorL0Npo, self.uprMinorL0Ctrl = createControl(
            "uprMinorL0", "uprMinorL0", npo, 18, "circle", 0.1)
        self.uprMinorL1Npo, self.uprMinorL1Ctrl = createControl(
            "uprMinorL1", "uprMinorL1", npo, 18, "circle", 0.1)
        self.uprMinorL2Npo, self.uprMinorL2Ctrl = createControl(
            "uprMinorL2", "uprMinorL2", npo, 18, "circle", 0.1)
        self.lwrMinorL0Npo, self.lwrMinorL0Ctrl = createControl(
            "lwrMinorL0", "lwrMinorL0", npo, 18, "circle", 0.1)
        self.lwrMinorL1Npo, self.lwrMinorL1Ctrl = createControl(
            "lwrMinorL1", "lwrMinorL1", npo, 18, "circle", 0.1)
        self.lwrMinorL2Npo, self.lwrMinorL2Ctrl = createControl(
            "lwrMinorL2", "lwrMinorL2", npo, 18, "circle", 0.1)

        self.cnrMinorR0Npo, self.cnrMinorR0Ctrl = createControl(
            "cnrMinorR0", "cnrMinorR0", npo, 20, "circle", 0.1)
        self.uprMinorR0Npo, self.uprMinorR0Ctrl = createControl(
            "uprMinorR0", "uprMinorR0", npo, 20, "circle", 0.1)
        self.uprMinorR1Npo, self.uprMinorR1Ctrl = createControl(
            "uprMinorR1", "uprMinorR1", npo, 20, "circle", 0.1)
        self.uprMinorR2Npo, self.uprMinorR2Ctrl = createControl(
            "uprMinorR2", "uprMinorR2", npo, 20, "circle", 0.1)
        self.lwrMinorR0Npo, self.lwrMinorR0Ctrl = createControl(
            "lwrMinorR0", "lwrMinorR0", npo, 20, "circle", 0.1)
        self.lwrMinorR1Npo, self.lwrMinorR1Ctrl = createControl(
            "lwrMinorR1", "lwrMinorR1", npo, 20, "circle", 0.1)
        self.lwrMinorR2Npo, self.lwrMinorR2Ctrl = createControl(
            "lwrMinorR2", "lwrMinorR2", npo, 20, "circle", 0.1)

        # Pinch Control
        npo = primitive.addTransform(self.ctlNpo, self.getName("pinch_npo"), t)
        self.uprPinchL0Npo, self.uprPinchL0Ctrl = createControl(
            "uprPinchL0", "uprPinchL0", npo, 18, "circle", 0.1)
        self.uprPinchR0Npo, self.uprPinchR0Ctrl = createControl(
            "uprPinchR0", "uprPinchR0", npo, 20, "circle", 0.1)
        self.lwrPinchL0Npo, self.lwrPinchL0Ctrl = createControl(
            "lwrPinchL0", "lwrPinchL0", npo, 18, "circle", 0.1)
        self.lwrPinchR0Npo, self.lwrPinchR0Ctrl = createControl(
            "lwrPinchR0", "lwrPinchR0", npo, 20, "circle", 0.1)

    def createJnt(self):
        pass

    def createNodesSDK(self):
        rootPos = transform.getTransformFromPos(self.guide.pos["root"])
        self.sdkNpo = primitive.addTransform(
            self.root, self.getName("SDK_npo"), rootPos)

        lipType = ["lips", "major", "minor", "corner"]
        for lip in lipType:
            lipTransform = primitive.addTransform(
                self.sdkNpo, "lips_" + lip + "_SDK_npo", rootPos)

            # Set each lipTransform as an instance variable
            setattr(self, lip + "NpoSDK", lipTransform)

        print("groups", self.groups)
        print("subgroups", self.subGroups)

        # major sdk
        for uprLwr, ctl in zip(["upr", "lwr"], [self.uprMajorC0Ctrl, self.lwrMajorC0Ctrl]):
            name = "{}Major_C0_SDK_buffer"
            bufferNode = primitive.addTransform(
                self.majorNpoSDK,
                name.format(uprLwr),
                rootPos)
            bufferNode.template.set(1)

            for xyz in "XYZ":
                ctl.attr("translate{}".format(xyz)) >> bufferNode.attr("translate{}".format(xyz))

                name = "{}Major_C0_translate{}_SDK{}"
                t = transform.getTransformFromPos(self.guide.pos["{}MajorC".format(uprLwr)])
                nodeNpo = primitive.addTransform(
                    self.majorNpoSDK,
                    name.format(uprLwr, xyz, "_npo"),
                    t)
                primitive.addTransform(
                    nodeNpo,
                    name.format(uprLwr, xyz, ""),
                    t)

        # minor sdk
        for uprLwr in ["upr", "lwr"]:
            sideGrpName = "{}Minor_SDK_npo"
            sideGrp = primitive.addTransform(self.minorNpoSDK, sideGrpName.format(uprLwr), rootPos)
            for side in ["L", "R"]:
                for i in range(0, 3):
                    ctlName = self.getName("{}Minor{}{}_ctl".format(uprLwr, side, i))
                    ctlNode = pm.PyNode(ctlName)

                    bufferName = "{}Minor_{}{}_SDK_buffer"
                    bufferNode = primitive.addTransform(
                        sideGrp,
                        bufferName.format(uprLwr, side, i),
                        rootPos)
                    bufferNode.template.set(1)

                    pos = self.guide.pos["{}Minor{}{}".format(uprLwr, side, i)]
                    t = transform.getTransformFromPos(pos)
                    for xyz in "XYZ":
                        ctlNode.attr("translate{}".format(xyz)) >> bufferNode.attr("translate{}".format(xyz))

                        name = "{}Minor_{}{}_translate{}_SDK{}"
                        nodeNpo = primitive.addTransform(
                            sideGrp,
                            name.format(uprLwr, side, i, xyz, "_npo"),
                            t)
                        primitive.addTransform(
                            nodeNpo,
                            name.format(uprLwr, side, i, xyz, ""),
                            t)

        # # corner sdk
        # for side in ["L", "R"]:
        #     bufferName = "cnr{}_major_SDK_buffer"
        #     bufferNode = primitive.addTransform(self.cornerNpoSDK,
        #                                         bufferName.format(side),
        #                                         rootPos)
        #     bufferNode.template.set(1)
        #     for xyz in "XYZ":
        #         # ctl.attr("translate{}".format(xyz)) >> bufferNode.attr("translate{}".format(xyz))
        #
        #         name = "cnr{}_major_translate{}_SDK{}"
        #         pos = self.guide.pos["{}_cnrLip".format(side)]
        #         t = transform.getTransformFromPos(pos)
        #         nodeNpo = primitive.addTransform(self.cornerNpo,
        #                                          self.getName(name.format(side, xyz, "_npo")),
        #                                          t)
        #         primitive.addTransform(nodeNpo,
        #                                self.getName(name.format(side, xyz, "")),
        #                                t)

        # lip sdk
        bufferNode = primitive.addTransform(self.lipsNpoSDK,
                                            "lip_C0_SDK_buffer",
                                            rootPos)
        bufferNode.template.set(1)

        for xyz in "XYZ":
            name = "lip_C0_translate{}_SDK{}"
            t = transform.getTransformFromPos(self.guide.pos["root"])
            nodeNpo = primitive.addTransform(self.lipsNpoSDK, name.format(xyz, "_npo"), t)
            primitive.addTransform(nodeNpo, name.format(xyz, ""), t)

        for xy in "XY":
            name = "lip_rotate{}_SDK{}"
            t = transform.getTransformFromPos(self.guide.pos["root"])
            nodeNpo = primitive.addTransform(self.lipsNpoSDK, name.format(xy, "_npo"), t)
            primitive.addTransform(nodeNpo, name.format(xy, ""), t)

    def setOutlineColor(self, node, xyz):
        node.useOutlinerColor.set(1)

        if "X" in xyz:
            new_color = (1.0, 0, 0)
        elif "Y" in xyz:
            new_color = (0, 1.0, 0)
        elif "Z" in xyz:
            new_color = (0.314, 0.314, 1.0)
        node.outlinerColor.set(new_color)

    # =====================================================
    # ATTRIBUTES
    # =====================================================
    def addAttributes(self):
        """Create the anim and setupr rig attributes for the component"""

        self.sideRotation_att = self.addAnimParam(
            "siderot", "Sides Rotation", "double", 20, 0, 100)
        self.vertRotation_att = self.addAnimParam(
            "vertrot", "Vertical Rotation", "double", 40, 0, 100)
        self.frontalTranslation_att = self.addAnimParam(
            "fronttrans", "Frontal Translation", "double", 1, 0, 1)
        self.verticalTranslation_att = self.addAnimParam(
            "verttrans", "Vertical Translation", "double", 0.2, 0, 1)
        self.followLips_att = self.addAnimParam(
            "floowlips", "FollowLips", "double", 0.05, 0, 1)
        self.lipsAlignSpeed_att = self.addAnimParam(
            "lipsAlignSpeed", "Lips Align Speed", "double", 10, 0, 100)

    # =====================================================
    # OPERATORS
    # =====================================================
    def addOperators(self):
        """Create operators and set the relations for the component rig

        Apply operators, constraints, expressions to the hierarchy.
        In order to keep the code clean and easier to debug,
        we shouldn't create any new object in this method.

        """
        print("parentComponent", self.guide.parentComponent)

        #
        # # mouth center rotation
        # pm.connectAttr(self.jaw_ctl + ".rotateZ",
        #                self.mouthCenter + ".rotateZ")
        #
        # # Node Creation ########
        #
        # # Mut Div nodes
        # md_node_1 = pm.createNode("multiplyDivide")
        # md_node_2 = pm.createNode("multiplyDivide")
        # md_node_3 = pm.createNode("multiplyDivide")
        # md_node_4 = pm.createNode("multiplyDivide")
        # md_node_5 = pm.createNode("multiplyDivide")
        # md_node_6 = pm.createNode("multiplyDivide")
        # md_node_7 = pm.createNode("multiplyDivide")
        # md_node_8 = pm.createNode("multiplyDivide")
        #
        # # Clamp o_node
        # clamp_node = pm.createNode("clamp")
        #
        # # Condition nodes
        # cond_node_1 = pm.createNode("condition")
        # cond_node_2 = pm.createNode("condition")
        # cond_node_3 = pm.createNode("condition")
        #
        # # Blend nodes
        # blend_node_1 = pm.createNode("blendColors")
        # blend_node_2 = pm.createNode("blendColors")
        #
        # # Node Conexions ########
        #
        # # md_node_1
        # pm.connectAttr(self.jaw_ctl + ".translateY", md_node_1 + ".input1X")
        # pm.connectAttr(self.vertRotation_att, md_node_1 + ".input2X")
        #
        # # md_node_2
        # pm.connectAttr(self.jaw_ctl + ".translateX", md_node_2 + ".input1X")
        # pm.connectAttr(self.sideRotation_att, md_node_2 + ".input2X")
        #
        # # md_node_3
        # pm.connectAttr(self.jaw_ctl + ".translateY", md_node_3 + ".input1X")
        # pm.connectAttr(self.lipsAlignSpeed_att, md_node_3 + ".input2X")
        #
        # # md_node_4
        # pm.connectAttr(self.jaw_ctl + ".translateY", md_node_4 + ".input1X")
        # pm.connectAttr(self.verticalTranslation_att, md_node_4 + ".input2X")
        #
        # # md_node_5
        # pm.connectAttr(self.jaw_ctl + ".translateZ", md_node_5 + ".input1X")
        # pm.connectAttr(self.frontalTranslation_att, md_node_5 + ".input2X")
        #
        # # md_node_6
        # pm.connectAttr(md_node_1 + ".outputX", md_node_6 + ".input1X")
        # pm.setAttr(md_node_6 + ".input2X", -1.0)
        #
        # # md_node_7
        # pm.connectAttr(md_node_5 + ".outputX", md_node_7 + ".input1X")
        # pm.connectAttr(clamp_node + ".outputR", md_node_7 + ".input2X")
        #
        # # md_node_8
        # pm.connectAttr(cond_node_2 + ".outColorR", md_node_8 + ".input1X")
        # pm.connectAttr(clamp_node + ".outputR", md_node_8 + ".input2X")
        #
        # # clamp_node
        # pm.connectAttr(md_node_3 + ".outputX", clamp_node + ".inputR")
        # pm.setAttr(clamp_node + ".maxR", 1.0)
        #
        # # cond_node_1
        # pm.connectAttr(md_node_6 + ".outputX", cond_node_1 + ".colorIfTrueR")
        # pm.connectAttr(md_node_6 + ".outputX", cond_node_1 + ".firstTerm")
        # pm.setAttr(cond_node_1 + ".operation", 4)
        # pm.setAttr(cond_node_1 + ".colorIfFalseR", 0)
        #
        # # cond_node_2
        # pm.connectAttr(md_node_2 + ".outputX", cond_node_2 + ".colorIfFalseR")
        # pm.connectAttr(md_node_6 + ".outputX", cond_node_2 + ".firstTerm")
        # pm.setAttr(cond_node_2 + ".operation", 2)
        #
        # # cond_node_3
        # pm.connectAttr(md_node_4 + ".outputX", cond_node_3 + ".colorIfTrueR")
        # pm.connectAttr(md_node_4 + ".outputX", cond_node_3 + ".firstTerm")
        # pm.setAttr(cond_node_3 + ".operation", 4)
        # pm.setAttr(cond_node_3 + ".colorIfFalseR", 0)
        #
        # # blend_node_1
        # pm.connectAttr(self.followLips_att, blend_node_1 + ".blender")
        # pm.connectAttr(md_node_6 + ".outputX", blend_node_1 + ".color1R")
        # pm.connectAttr(md_node_2 + ".outputX", blend_node_1 + ".color1G")
        # pm.connectAttr(cond_node_1 + ".outColorR", blend_node_1 + ".color2R")
        # pm.connectAttr(md_node_8 + ".outputX", blend_node_1 + ".color2G")
        #
        # # blend_node_2
        # pm.connectAttr(self.followLips_att, blend_node_2 + ".blender")
        # pm.connectAttr(cond_node_3 + ".outColorR", blend_node_2 + ".color1R")
        # pm.connectAttr(md_node_5 + ".outputX", blend_node_2 + ".color1G")
        # pm.connectAttr(md_node_7 + ".outputX", blend_node_2 + ".color2G")
        #
        # # inputs to transforms
        #
        # pm.connectAttr(md_node_6 + ".outputX", self.jawLow_rot + ".rotateX")
        # pm.connectAttr(md_node_2 + ".outputX", self.jawLow_rot + ".rotateY")
        #
        # pm.connectAttr(blend_node_1 + ".outputR", self.jawUp_rot + ".rotateX")
        # pm.connectAttr(blend_node_1 + ".outputG", self.jawUp_rot + ".rotateY")
        #
        # pm.connectAttr(cond_node_3 + ".outColorR",
        #                self.jawLow_pos + ".translateY")
        # pm.connectAttr(md_node_5 + ".outputX",
        #                self.jawLow_pos + ".translateZ")
        #
        # pm.connectAttr(blend_node_2 + ".outputR",
        #                self.jawUp_pos + ".translateY")
        # pm.connectAttr(blend_node_2 + ".outputG",
        #                self.jawUp_pos + ".translateZ")

    # =====================================================
    # CONNECTOR
    # =====================================================
    def setRelation(self):
        """Set the relation beetween object from guide to rig"""
        pass
        # self.relatives["root"] = self.root
        # self.relatives["jaw"] = self.jawLow_rot
        # self.relatives["rotcenter"] = self.jawLow_rot
        # self.relatives["lipup"] = self.lipup_ctl
        # self.relatives["liplow"] = self.liplow_ctl
        #
        # self.controlRelatives["root"] = self.parentCtlTag
        # self.controlRelatives["jaw"] = self.jaw_ctl
        # self.controlRelatives["rotcenter"] = self.jaw_ctl
        # self.controlRelatives["lipup"] = self.lipup_ctl
        # self.controlRelatives["liplow"] = self.liplow_ctl
        #
        # self.jointRelatives["root"] = 0
        # self.jointRelatives["jaw"] = 0
        # self.jointRelatives["rotcenter"] = 0
        # self.jointRelatives["lipup"] = 1
        # self.jointRelatives["liplow"] = 2
