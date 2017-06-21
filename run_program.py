#! /usr/bin/env python
import sys
from PyQt5 import QtWidgets

from PVWatts_Tool import PVWatts_API


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.first_run = True
        container = QtWidgets.QHBoxLayout()

        left_pane = QtWidgets.QVBoxLayout()

        parameters = QtWidgets.QHBoxLayout()
        param_labels = QtWidgets.QVBoxLayout()
        param_fields = QtWidgets.QVBoxLayout()

        self.area_l = QtWidgets.QLabel("Area: ")
        self.module_l = QtWidgets.QLabel("Module Type: ")
        self.lat_l = QtWidgets.QLabel("Lat: ")
        self.lon_l = QtWidgets.QLabel("Lon: ")
        self.losses_l = QtWidgets.QLabel("Losses: ")
        self.array_l = QtWidgets.QLabel("Array Type: ")
        self.tilt_l = QtWidgets.QLabel("Tilt")
        self.azimuth_l = QtWidgets.QLabel("Azimuth: ")

        param_labels.addWidget(self.area_l)
        param_labels.addWidget(self.module_l)
        param_labels.addWidget(self.lat_l)
        param_labels.addWidget(self.lon_l)
        param_labels.addWidget(self.losses_l)
        param_labels.addWidget(self.array_l)
        param_labels.addWidget(self.tilt_l)
        param_labels.addWidget(self.azimuth_l)

        self.area_le = QtWidgets.QLineEdit("1000")
        self.module_le = QtWidgets.QComboBox()
        self.module_le.insertItems(0, ["0", "1", "2"])
        self.lat_le = QtWidgets.QLineEdit("42.3")
        self.lon_le = QtWidgets.QLineEdit("-83.7")
        self.losses_le = QtWidgets.QLineEdit("14")
        self.array_le = QtWidgets.QComboBox()
        self.array_le.insertItems(0, ["0", "1", "2", "3", "4"])
        self.tilt_le = QtWidgets.QLineEdit("34")
        self.azimuth_le = QtWidgets.QLineEdit("180")

        param_fields.addWidget(self.area_le)
        param_fields.addWidget(self.module_le)
        param_fields.addWidget(self.lat_le)
        param_fields.addWidget(self.lon_le)
        param_fields.addWidget(self.losses_le)
        param_fields.addWidget(self.array_le)
        param_fields.addWidget(self.tilt_le)
        param_fields.addWidget(self.azimuth_le)

        self.submit = QtWidgets.QPushButton("Submit")

        parameters.addLayout(param_labels)
        parameters.addLayout(param_fields)

        left_pane.addLayout(parameters)
        left_pane.addWidget(self.submit)

        self.output_box = QtWidgets.QPlainTextEdit()
        self.output_box.setFixedWidth(500)

        container.addLayout(left_pane)
        container.addWidget(self.output_box)

        self.submit.clicked.connect(self.run)
        self.setLayout(container)
        self.setWindowTitle("PV Watts Tool")
        self.show()

    def run(self):
        global run
        run = PVWatts_API.PVWatts_Run(area=int(self.area_le.text()),
                                      module_type=int(self.module_le.currentText()),
                                      lat=self.lat_le.text(),
                                      lon=self.lon_le.text(),
                                      losses=self.losses_le.text(),
                                      array_type=self.array_le.currentText(),
                                      tilt=self.tilt_le.text(),
                                      azimuth=self.azimuth_le.text(),
                                      timeframe='hourly')
        if self.first_run:
            self.output_box.appendPlainText(run.describe())
            self.first_run = False
        else:
            self.output_box.appendPlainText('\n' + run.describe())


def go():
    app = QtWidgets.QApplication(sys.argv)
    current_run = Window()
    sys.exit(app.exec())
