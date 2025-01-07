import os
import sys
import oracledb

from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QHeaderView

from CDUIWidgets.CDUIWidgets import CDUITable

import settings
import models

oracledb.init_oracle_client()


def toggle_connection():
    if settings.SETTINGS['CONNECTION'] is None:
        DIALECT = 'oracle'
        SQL_DRIVER = 'oracledb'
        USERNAME = os.environ.get('DATABASE_USER')  # enter your username
        PASSWORD = os.environ.get('DATABASE_PASS')  # enter your password
        HOST = os.environ.get('DATABASE_HOST')  # enter the oracle db host url
        PORT = os.environ.get('DATABASE_PORT')  # enter the oracle port number
        SERVICE = os.environ.get('DATABASE_NAME')  # enter the oracle db service name
        ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(
            PORT) + '/?service_name=' + SERVICE

        settings.SETTINGS['CONNECTION'] = engine.create_engine(ENGINE_PATH_WIN_AUTH)
        label.setText("<h1>Connected</h1>")
        btn_connect.setText("Disconnect")
    else:
        settings.SETTINGS['CONNECTION'] = None
        label.setText("<h1>Not Connected</h1>")
        btn_connect.setText("Connect")


def get_chief():
    Session = sessionmaker(settings.SETTINGS['CONNECTION'])

    with Session.begin() as session:
        chiefs = [(c.last_name, c.first_name) for c in session.query(models.ChiefScientist).all()]

    table.setHeader(['last_name', 'first_name'])
    table.setRowCount(len(chiefs))

    for row, chief in enumerate(chiefs):
        for col, value in enumerate(chief):
            table.setItem(row, col, QTableWidgetItem(str(value).strip()))

    table.resizeColumnsToContents()


app = QApplication([])

window = QWidget()
window.setWindowTitle("Cruse Database UI (CDUI)")

layout = QVBoxLayout(window)
btn_layout = QHBoxLayout(window)

label = QLabel("<h1>Not Connected</h1>", parent=window)
btn_connect = QPushButton("Connect", parent=window)
btn_connect.clicked.connect(toggle_connection)

btn_chief = QPushButton("Get Chief Scientists", parent=window)
btn_chief.clicked.connect(get_chief)

table = CDUITable(parent=window)

layout.addWidget(label)
layout.addWidget(table)
layout.addWidget(btn_connect)
layout.addWidget(btn_chief)

window.show()

sys.exit(app.exec())
