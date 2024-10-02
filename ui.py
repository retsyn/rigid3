'''
ui.py
Created: Monday, 19th September 2022 9:02:34 am
Matthew Riche
Last Modified: Tuesday, 22nd November 2022 2:34:58 pm
Modified By: Matthew Riche
'''

import maya.OpenMayaUI as omui
import maya.cmds as cmds
import sys
import os
from PySide2 import QtCore, QtWidgets as qtw, QtGui, QtUiTools
from shiboken2 import wrapInstance

from . import globals
from . import file_ops as fo
from . import controls as ctl
from . import build as bld
from . import nodework as nw

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), qtw.QWidget)


class Rigid_ui(qtw.QDialog):
    def __init__(self, parent = maya_main_window()):
        super(Rigid_ui, self).__init__(parent)

        self.setWindowTitle("Rigid v{}".format(globals.RIGID_VERSION))

        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self._init_ui()
        self._populate_and_edit_widgets()
        self._create_connections()

        # init the load path.
        mod_path = os.path.abspath(__file__)
        parent_path = os.path.dirname(mod_path)
        self.ctrls_path = ("{}/control_shapes/".format(parent_path))


        # This UI will own a piece of controller data of it's own, for controller shape edits.
        self.ui_ctl_data = ctl.CurveData()
        self.show()

        # Copied colour state:
        self.copied_colour = (0.2, 0.2, 0.2)

        return

    def _refresh(self):

        # Update the current curve:
        pass


    def _init_ui(self):
        """The UI class for the main window-- connects to .ui content and arranges for it's
        connection and instantiation.
        """        

        mod_path = os.path.abspath(__file__)
        parent_path = os.path.dirname(mod_path)
        print("Rigid path is \"{}\"".format(parent_path))

        ui_file = QtCore.QFile("{}/uis/rigid_main.ui".format(parent_path))
        ui_file.open(QtCore.QFile.ReadOnly)
        
        qss_file = QtCore.QFile(f"{parent_path}/uis/rtech.qss")
        if qss_file.open(QtCore.QFile.ReadOnly):
            qss_content = qss_file.readAll()
            qss_file.close()

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file, parentWidget=self)
        self.setStyleSheet(str(qss_content, encoding='utf-8'))

        self.vis_copydata_button = self.findChild(qtw.QPushButton, "copy_data_button")
        self.vis_buildorigin_button = self.findChild(qtw.QPushButton, "build_button")
        self.vis_make_at_match_button = self.findChild(qtw.QPushButton, "build_match_button")
        self.vis_replace_button = self.findChild(qtw.QPushButton, "replace_sel_button")
        self.vis_load_curvedata = self.findChild(qtw.QPushButton, "load_data_button")
        self.vis_save_curvedata = self.findChild(qtw.QPushButton, "save_data_button")
        self.vis_mirrorx_button = self.findChild(qtw.QPushButton, "mirror_x_button")
        self.vis_mirrory_button = self.findChild(qtw.QPushButton, "mirror_y_button")
        self.vis_mirrorz_button = self.findChild(qtw.QPushButton, "mirror_z_button")
        self.bld_fastfk_button = self.findChild(qtw.QPushButton, "fast_fk_button")
        self.bld_ribbon_joints_button = self.findChild(qtw.QPushButton, "ribbon_joints_button")

        self.setblue_button = self.findChild(qtw.QPushButton, "blue_pushbutton")
        self.setgreen_button = self.findChild(qtw.QPushButton, "green_pushbutton")
        self.setpaleblue_button = self.findChild(qtw.QPushButton, "paleblue_pushbutton")
        self.setpalered_button = self.findChild(qtw.QPushButton, "palered_pushbutton")
        self.setblack_button = self.findChild(qtw.QPushButton, "black_pushbutton")
        self.setpurple_button = self.findChild(qtw.QPushButton, "purple_pushbutton")
        self.setred_button = self.findChild(qtw.QPushButton, "red_pushbutton")
        self.setyellow_button = self.findChild(qtw.QPushButton, "yellow_pushbutton")
        self.setpaleyellow_button = self.findChild(qtw.QPushButton, "paleyellow_pushbutton")

        self.copycolour_button = self.findChild(qtw.QPushButton, "copycolour_button")
        self.pastecolour_button = self.findChild(qtw.QPushButton, "pastecolour_button")
        self.thicken25_button = self.findChild(qtw.QPushButton, "thicken25_button")
        self.thicken40_button = self.findChild(qtw.QPushButton, "thicken40_button")
        self.unthicken_button = self.findChild(qtw.QPushButton, "unthicken_button")


        self.curvedata_label = self.findChild(qtw.QLabel, "cur_data_label")

        return

    def _populate_and_edit_widgets(self):
        '''
        Upon instantiation, some widgets need population based on file content, and some text will
        represent non-static info.
        '''
        pass

    def _create_connections(self):

        self.vis_copydata_button.clicked.connect(self._vis_copy_data)
        self.vis_buildorigin_button.clicked.connect(self._vis_build_origin)
        self.vis_make_at_match_button.clicked.connect(self._vis_build_match)
        self.vis_replace_button.clicked.connect(self._vis_replace_sel)
        self.vis_load_curvedata.clicked.connect(self._vis_load_data)
        self.vis_save_curvedata.clicked.connect(self._vis_save_data)
        self.bld_fastfk_button.clicked.connect(self._bld_fast_fk)
        self.bld_ribbon_joints_button.clicked.connect(self._bld_ribbon_joints)

        self.vis_mirrorx_button.clicked.connect(lambda: self._vis_mirror_ctrl(axis='x'))
        self.vis_mirrory_button.clicked.connect(lambda: self._vis_mirror_ctrl(axis='y'))
        self.vis_mirrorz_button.clicked.connect(lambda: self._vis_mirror_ctrl(axis='z'))

        self.thicken25_button.clicked.connect(lambda: self._thicken25())
        self.thicken40_button.clicked.connect(lambda: self._thicken40())
        self.unthicken_button.clicked.connect(lambda: self._unthicken())

        self.setblue_button.clicked.connect(lambda:self._set_rgb(globals.rgb_blue))
        self.setgreen_button.clicked.connect(lambda:self._set_rgb(globals.rgb_green))
        self.setpaleblue_button.clicked.connect(lambda:self._set_rgb(globals.rgb_paleblue))
        self.setpalered_button.clicked.connect(lambda:self._set_rgb(globals.rgb_palered))
        self.setblack_button.clicked.connect(lambda:self._set_rgb(globals.rgb_black))
        self.setpurple_button.clicked.connect(lambda:self._set_rgb(globals.rgb_purple))
        self.setred_button.clicked.connect(lambda:self._set_rgb(globals.rgb_red))
        self.setpaleyellow_button.clicked.connect(lambda:self._set_rgb(globals.rgb_paleyellow))
        self.setyellow_button.clicked.connect(lambda:self._set_rgb(globals.rgb_yellow))

        self.pastecolour_button.clicked.connect(lambda:self._set_rgb(self.copied_colour))


        self.copycolour_button.clicked.connect(lambda: self._copy_colour())

    def _copy_colour(self):

        selection = cmds.ls(sl=True)[0]

        shape = nw.get_shape(selection)[0]

        colourrgb = cmds.getAttr(f"{shape}.overrideColorRGB")[0]
        self.copied_colour = colourrgb
        r, g, b = [int(value * 255) for value in colourrgb]
        new_colour = QtGui.QColor(r, g, b)
        self.pastecolour_button.setStyleSheet(f"background-color: rgb({new_colour.red()}, {new_colour.green()}, {new_colour.blue()});")
        


    def _unthicken(self):

        selection = cmds.ls(sl=True)
        for node in selection:
            try:
                shape = nw.get_shape(node)[0]
            except TypeError:
                shape = node
            
            cmds.setAttr(shape + ".lineWidth", -1.0)
            print(f"Set {shape} to thickness -1.0")

    def _thicken25(self):

        selection = cmds.ls(sl=True)
        for node in selection:
            try:
                shape = nw.get_shape(node)[0]
            except TypeError:
                shape = node
            
            cmds.setAttr(shape + ".lineWidth", 2.5)
            print(f"Set {shape} to thickness 2.5")


    def _thicken40(self):

        selection = cmds.ls(sl=True)
        for node in selection:
            try:
                shape = nw.get_shape(node)[0]
            except TypeError:
                shape = node
            
            cmds.setAttr(shape + ".lineWidth", 4.0)
            print(f"Set {shape} to thickness 4.0")


    def _set_rgb(self, rgb_value):
        print(f"Recoloured to {rgb_value}")
        selections = cmds.ls(sl=True)
        for node in selections:
            try:
                shape = nw.get_shape(node)[0]
            except TypeError:
                shape = node
            cmds.setAttr(f"{shape}.overrideEnabled", 1)
            cmds.setAttr(f"{shape}.overrideRGBColors", 1)
            
            cmds.setAttr(f"{shape}.overrideColorR", rgb_value[0])
            cmds.setAttr(f"{shape}.overrideColorG", rgb_value[1])
            cmds.setAttr(f"{shape}.overrideColorB", rgb_value[2])

    def _recolor(self, index):
        
        selections = cmds.ls(sl=True)
        # Find a shape node if there is one:
        for node in selections:
            try:
                shape = nw.get_shape(node)[0]
            except TypeError:
                shape = node

            cmds.setAttr(shape + '.overrideEnabled', 1)
            cmds.setAttr(shape + '.overrideColor', index)  
            print("New colour index {}".format(index))          


    def _vis_copy_data(self):
        """Trigged by copy data from the UI-- copies selected curve into workable data.
        """        
        
        if(len(cmds.ls(sl=True)) == 0):
            cmds.inViewMessage(amg='<hl>Must select a nurbsCurve.</hl>', pos='midCenter', fade=True)

        try:
            self.ui_ctl_data.capture_curve(sel=True)
            print("self curve data is {}".format(self.ui_ctl_data.curve_shape))
        except TypeError:
            cmds.inViewMessage(amg="<hl>Must be a nurbsCurve.</hl>", pos='midCenter', fade=True)
        
        self.curvedata_label.setText("copied\n{}".format(self.ui_ctl_data.curve_shape))

    def _vis_build_origin(self):
        """UI wrapper for the curveData.build() method.
        """        
        self.ui_ctl_data.build()

    def _vis_build_match(self):

        sel = cmds.ls(sl=True)
        if(sel):
            if(cmds.objectType(sel[0]) not in ['transform', 'joint']):
                cmds.inViewMessage(amg="<hl>Can't match to a non-transform!</hl>", pos='midCenter',
                    fade=True)
                return
            self.ui_ctl_data.build()
            new_null = cmds.group(self.ui_ctl_data.curve_node)
            token = sel[0].rpartition('_')[0]
            cmds.matchTransform(new_null, sel[0])
            cmds.rename(new_null, '{}_null'.format(token))
            cmds.rename(self.ui_ctl_data.curve_node, '{}_ctrl'.format(token))
        else:
            cmds.inViewMessage(amg="<hl>Must make a selection</hl>")

    def _vis_replace_sel(self):
        """UI wrapper for the curveData.replace() method.
        """        
        self.ui_ctl_data.replace()

    def _vis_load_data(self):
        """Opens a filedialog browser, and reads the JSON data selected into the curveData.
        """        
        load_path = self._browse(title='Load JSON Curve Data', save=False, dir=self.ctrls_path)
        data_dict = fo.read_from_file(load_path)
        print("Loaded data contents:\n{}".format(data_dict))
        try:
            self.ui_ctl_data.from_dict(data_dict)
        except TypeError:
            print("Loaded empty data!")
        except ValueError:
            print("Loaded empty data!")

    def _vis_save_data(self):
        """Opens a filedialog browser, and saves the captured curve data as JSON.
        """        

        try:
            data_dict = self.ui_ctl_data.as_dict()
        except (ValueError, TypeError):
            if(len(cmds.ls(sl=True)) == 1):
                self.ui_ctl_data.capture_curve(sel=True)
                data_dict = self.ui_ctl_data.as_dict()
            else:
                cmds.inViewMessage(amg="<hl>Capture curve data or select a viable curve.</hl>", 
                    pos='midCenter', fade=True)
                return

        save_path = self._browse(title='Save Curve Data as JSON', save=True, dir=self.ctrls_path)
        fo.dump_to_file(data_dict, save_path)

    def _vis_mirror_ctrl(self, axis):
        """Invoke the mirror function of self.ui_ctrl_data from a button.
        Args:
            axis (str ['x', 'y', 'z']): Which axis to mirror on.
        """        
        self.ui_ctl_data.mirror(axis=axis)
        old_text = self.curvedata_label.text()
        new_text = old_text + ("\nMirrored on {}".format(axis))
        self.curvedata_label.setText(new_text)


    def _bld_fast_fk(self):
        """Invoke the SimpleFK build.
        """        

        #TODO The UI should hold onto the idiom data for records.
        bld.SimpleFK()

    def _bld_ribbon_joints(self):
        """Invoke the ribbon joints build.
        """        

        bld.RibbonJoints()

    def _browse(self, title='Open Maya File', save=True, dir=''):
        """Wraps the opening of a file browser window.
        
        Args:
            title (str, optional): Dialog title text. Defaults to 'Open Maya File'.
            save (bool, optional): Bool; True=Save mode, False=Load. Defaults to True.
            dir (str, optional): Default directory. Defaults to ''.

        Returns:
            str: Path to specified file.
        """        

        if(save):
            fname = qtw.QFileDialog.getSaveFileName(
                self, title, dir, "Curve Data (*.json)")[0]
        else:
            fname = qtw.QFileDialog.getOpenFileName(
                self, title, dir, "Curve Data (*.json)")[0]
        if(fname):
            return fname