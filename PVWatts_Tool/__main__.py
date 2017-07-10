#! /usr/bin/env python
import sys
import os
import pandas
from PyQt5 import QtWidgets

from PVWatts_Tool import PVWatts_API

__author__ = "warnuk"
__credits__ = ["warnuk", "NREL", "PVWatts"]
__license__ = "MIT"
__version__ = "1.0.5"
__maintainer__ = "warnuk"
__email__ = "warnuk@umich.edu"
__status__ = "Development"

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """ Initialize the Graphical User Interface.

        The GUI consists of a main container, a parameter pane (with labels and fields), and an output pane.
        The submit button creates a new instance of a pvwatts_run object. The pvwatts_run object calls NREL APIs using
        user-input to generate solar potential estimates and rate/utility information. This info is then output to the
        output box on the right side of the container."""

        self.first_run = True
        container = QtWidgets.QVBoxLayout()
        subcontainer = QtWidgets.QHBoxLayout()

        left_pane = QtWidgets.QVBoxLayout()
        right_pane = QtWidgets.QVBoxLayout()

        parameters = QtWidgets.QHBoxLayout()
        param_labels = QtWidgets.QVBoxLayout()
        param_fields = QtWidgets.QVBoxLayout()

        self.api_l = QtWidgets.QLabel("API Key: ")
        self.area_l = QtWidgets.QLabel("Area (m^2): ")
        self.module_l = QtWidgets.QLabel("Module Type: ")
        self.lat_l = QtWidgets.QLabel("Lat (+/- °): ")
        self.lon_l = QtWidgets.QLabel("Lon (+/- °): ")
        self.losses_l = QtWidgets.QLabel("Losses (%): ")
        self.array_l = QtWidgets.QLabel("Array Type: ")
        self.tilt_l = QtWidgets.QLabel("Tilt (°)")
        self.azimuth_l = QtWidgets.QLabel("Azimuth (°): ")
        self.rate_l = QtWidgets.QLabel("Rate Type: ")
        self.incentivized_l = QtWidgets.QLabel("LCOE with Tax Credits: ")

        param_labels.addWidget(self.api_l)
        param_labels.addWidget(self.area_l)
        param_labels.addWidget(self.module_l)
        param_labels.addWidget(self.lat_l)
        param_labels.addWidget(self.lon_l)
        param_labels.addWidget(self.losses_l)
        param_labels.addWidget(self.array_l)
        param_labels.addWidget(self.tilt_l)
        param_labels.addWidget(self.azimuth_l)
        param_labels.addWidget(self.rate_l)
        param_labels.addWidget(self.incentivized_l)

        self.api_le = QtWidgets.QLineEdit()
        self.area_le = QtWidgets.QLineEdit("1000")
        self.module_le = QtWidgets.QComboBox()
        self.module_le.insertItems(0, ["Standard", "Premium", "Thin Film"])
        self.lat_le = QtWidgets.QLineEdit("42.3")
        self.lon_le = QtWidgets.QLineEdit("-83.7")
        self.losses_le = QtWidgets.QLineEdit("14")
        self.array_le = QtWidgets.QComboBox()
        self.array_le.insertItems(0, ["Fixed - Open Rack", "Fixed - Roof Mounted", "1-Axis",
                                      "1-Axis Backtracking", "2-Axis"])
        self.tilt_le = QtWidgets.QLineEdit("34")
        self.azimuth_le = QtWidgets.QLineEdit("180")
        self.rate_le = QtWidgets.QComboBox()
        self.rate_le.insertItems(0, ["Residential", "Commercial", "Industrial"])
        self.incentivized_cb = QtWidgets.QComboBox()
        self.incentivized_cb.insertItems(0, ["Yes", "No"])

        param_fields.addWidget(self.api_le)
        param_fields.addWidget(self.area_le)
        param_fields.addWidget(self.module_le)
        param_fields.addWidget(self.lat_le)
        param_fields.addWidget(self.lon_le)
        param_fields.addWidget(self.losses_le)
        param_fields.addWidget(self.array_le)
        param_fields.addWidget(self.tilt_le)
        param_fields.addWidget(self.azimuth_le)
        param_fields.addWidget(self.rate_le)
        param_fields.addWidget(self.incentivized_cb)

        parameters.addLayout(param_labels)
        parameters.addLayout(param_fields)

        left_pane.addLayout(parameters)

        self.output_box = QtWidgets.QPlainTextEdit()
        self.output_box.setFixedWidth(500)

        right_pane.addWidget(self.output_box)

        subcontainer.addLayout(left_pane)
        subcontainer.addLayout(right_pane)

        output_layout = QtWidgets.QHBoxLayout()
        self.output_l = QtWidgets.QLabel("Save hourly data to file: ")
        self.savefilepath = QtWidgets.QLineEdit()
        self.fileselect = QtWidgets.QPushButton("Save as...")
        output_layout.addWidget(self.output_l)
        output_layout.addWidget(self.savefilepath)
        output_layout.addWidget(self.fileselect)

        self.submit = QtWidgets.QPushButton("Submit")

        container.addLayout(subcontainer)
        container.addLayout(output_layout)
        container.addWidget(self.submit)

        self.fileselect.clicked.connect(self.set_output_file)
        self.submit.clicked.connect(self.generate_output)
        self.setLayout(container)
        self.setWindowTitle("PVWatts Tool")
        self.show()

    def set_output_file(self):
        destination = str(QtWidgets.QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')[0])
        self.savefilepath.setText(destination)

    def module_type(self):
        """Convert descriptive user-input into PVWatts API input parameters.

        PVWatts requires numeric input for the module type parameter; this method allows the user to select from
        more descriptive options and generate the required input parameter."""

        if self.module_le.currentText() == "Standard":
            moduletype_id = "0"
        elif self.module_le.currentText() == "Premium":
            moduletype_id = "1"
        elif self.module_le.currentText() == "Thin Film":
            moduletype_id = "2"
        return (moduletype_id)

    def array_type(self):
        """Convert descriptive user-input into PVWatts API input parameters.

        PVWatts requires numeric input for the array type parameter; this method allows the user to select from
        more descriptive options and generate the required input parameter."""

        if self.array_le.currentText() == "Fixed - Open Rack":
            arraytype_id = "0"
        elif self.array_le.currentText() == "Fixed - Roof Mounted":
            arraytype_id = "1"
        elif self.array_le.currentText() == "1-Axis":
            arraytype_id = "2"
        elif self.array_le.currentText() == "1-Axis Backtracking":
            arraytype_id = "3"
        elif self.array_le.currentText() == "2-Axis":
            arraytype_id = "4"
        return (arraytype_id)

    def incentivized(self):
        if self.incentivized_cb.currentText() == "Yes":
            return(True)
        else:
            return (False)

    def generate_output(self):
        """Creates a global scenario object and prints descriptive information to the output box."""

        global scenario
        scenario = PVWatts_API.PVWatts_Run(api_key=self.api_le.text(),
                                           area=float(self.area_le.text()),
                                           module_type=int(self.module_type()),
                                           lat=self.lat_le.text(),
                                           lon=self.lon_le.text(),
                                           losses=self.losses_le.text(),
                                           array_type=self.array_type(),
                                           tilt=self.tilt_le.text(),
                                           azimuth=self.azimuth_le.text(),
                                           timeframe='hourly',
                                           ratetype=self.rate_le.currentText().lower(),
                                           incentivized=self.incentivized())

        if self.first_run:
            self.output_box.appendPlainText(scenario.describe())
            self.first_run = False
        else:
            self.output_box.appendPlainText('--------------------' + '\n' + scenario.describe())

        if self.savefilepath.text():
            scenario.hourly_data.to_csv(self.savefilepath.text())

def run():
    """Make GUI call-able from python interpreter.

    The user can initialize the GUI from a python interpreter by calling PVWatts_Tool.run()"""

    app = QtWidgets.QApplication(sys.argv)
    current_run = Window()
    sys.exit(app.exec())

run()