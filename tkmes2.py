from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QLabel, QApplication, QMainWindow

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = ClickableLabel("Click me")
        self.label.clicked.connect(self.on_label_clicked)
        self.setCentralWidget(self.label)

    def on_label_clicked(self):
        print("Label clicked!")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
