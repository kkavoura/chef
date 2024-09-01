from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Global Stylesheet Example")

        # Create a central widget and set a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Add some buttons to demonstrate the global stylesheet
        button1 = QPushButton("Button 1", self)
        button2 = QPushButton("Button 2", self)
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setCentralWidget(central_widget)
        self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Set a global stylesheet
    app.setStyleSheet("""
        QPushButton {
            background-color: lightblue;
            border: 2px solid gray;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: lightgreen;
        }
    """)

    mainWin = MainWindow()
    sys.exit(app.exec())