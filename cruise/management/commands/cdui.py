import logging

from cdui.CDUIWidgets import CDUIMainWindow
from PyQt6.QtWidgets import QApplication
from django.core.management.base import BaseCommand

logger = logging.getLogger('cdui')


class Command(BaseCommand):

    help = "Runs the standalone application without a web interface"

    def handle(self, *args, **options):

        app = QApplication([])
        logger.debug("Application initialized")

        window = CDUIMainWindow()
        window.show()

        app.exec()
        logger.debug("Application closing")
