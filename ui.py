'''
ui.py
Created: Monday, 19th September 2022 9:02:34 am
Matthew Riche
Last Modified: Monday, 19th September 2022 9:03:54 am
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

        # This UI will own a piece of controller data of it's own, for controller shape edits.
        self.ui_ctl_data = ctl.CurveData()
        self.show()

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

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file, parentWidget=self)

        self.vis_copydata_button = self.findChild(qtw.QPushButton, "copy_data_button")
        self.vis_buildorigin_button = self.findChild(qtw.QPushButton, "build_button")
        self.vis_replace_button = self.findChild(qtw.QPushButton, "replace_sel_button")
        self.vis_load_curvedata = self.findChild(qtw.QPushButton, "load_data_button")
        self.vis_save_curvedata = self.findChild(qtw.QPushButton, "save_data_button")
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
        self.vis_replace_button.clicked.connect(self._vis_replace_sel)
        self.vis_load_curvedata.clicked.connect(self._vis_load_data)
        self.vis_save_curvedata.clicked.connect(self._vis_save_data)


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

    def _vis_replace_sel(self):
        """UI wrapper for the curveData.replace() method.
        """        
        self.ui_ctl_data.replace()

    def _vis_load_data(self):
        """Opens a filedialog browser, and reads the JSON data selected into the curveData.
        """        
        load_path = self._browse(title='Load JSON Curve Data', save=False)
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

        save_path = self._browse(title='Save Curve Data as JSON', save=True)
        fo.dump_to_file(data_dict, save_path)

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