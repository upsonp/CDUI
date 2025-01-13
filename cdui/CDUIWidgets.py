from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QLabel, QTableWidget, QHBoxLayout, QTableWidgetItem, \
    QWidget
from cruise import models as cruise_models

import logging

logger = logging.getLogger('django')


class CDUIMainWindow(QWidget):

    def get_table(self):
        return self.table

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cruise Database UI')

        layout = QVBoxLayout(self)
        btn_layout = QHBoxLayout(self)

        self.table = CDUITable(parent=self)

        btn_chief = QPushButton("Chief Scientists", parent=self)
        btn_chief.clicked.connect(lambda: get_data(self.table, cruise_models.ChiefScientist))

        btn_data_type = QPushButton("Data Types", parent=self)
        btn_data_type.clicked.connect(lambda: get_data(self.table, cruise_models.DataType))

        btn_delivery = QPushButton("Delivery Stage", parent=self)
        btn_delivery.clicked.connect(lambda: get_data(self.table, cruise_models.DeliveryStage))

        btn_process = QPushButton("Process State", parent=self)
        btn_process.clicked.connect(lambda: get_data(self.table, cruise_models.ProcessState))

        btn_cruise = QPushButton("Cruise", parent=self)
        btn_cruise.clicked.connect(lambda: get_data(self.table, cruise_models.Cruise))

        btn_data = QPushButton("Data", parent=self)
        btn_data.clicked.connect(lambda: get_data(self.table, cruise_models.Data))

        btn_layout.addWidget(btn_chief)
        btn_layout.addWidget(btn_data_type)
        btn_layout.addWidget(btn_delivery)
        btn_layout.addWidget(btn_process)
        btn_layout.addWidget(btn_cruise)
        btn_layout.addWidget(btn_data)

        layout.addWidget(self.table)
        layout.addLayout(btn_layout)


class CDUITable(QTableWidget):

    def __init__(self, parent=None):
        super(CDUITable, self).__init__(parent)

        self.horizontalHeader().setStyleSheet("::section {background-color: lightGray; }")
        self.verticalHeader().setStyleSheet("::section {background-color: lightGray; }")

    def setHeader(self, header: list):
        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)


def getFieldName(field):
    if hasattr(field, 'verbose_name'):
        return getattr(field, 'verbose_name')

    return field.name


def get_data(table: CDUITable, model: any):
    logger.debug("Getting rows for model: %s", model)
    table_rows = model.objects.using('cruise_database').all()

    logger.debug("Rows: %d", len(table_rows))
    fields = model._meta.fields
    table.setHeader([getFieldName(field) for field in fields])
    table.setRowCount(len(table_rows))

    for row_number, row in enumerate(table_rows):
        for col, value in enumerate(fields):
            table.setItem(row_number, col, QTableWidgetItem(str(getattr(row, value.name)).strip()))

    table.resizeColumnsToContents()


