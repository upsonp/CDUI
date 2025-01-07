from PyQt6.QtWidgets import QTableWidget


class CDUITable(QTableWidget):

    def __init__(self, parent=None):
        super(CDUITable, self).__init__(parent)

        self.horizontalHeader().setStyleSheet("::section {background-color: lightGray; }")
        self.verticalHeader().setStyleSheet("::section {background-color: lightGray; }")

    def setHeader(self, header: list):
        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
