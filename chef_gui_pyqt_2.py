import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
    QLineEdit,
    QToolBar,
    QStatusBar,
    QPushButton,
    QGroupBox,
    QScrollArea
)

from PyQt6.QtCore import Qt
from manager import Manager
# from functools import partial 
from typing import Callable, Type

guiManager = Manager()
buttonLineEditPairs = {}


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        # Create widgets
        self.centralWidget = QWidget()
        self.inputWidget = self._createDataInputWidget()
        self.scrollArea = QScrollArea()
        self.displayWidget = QWidget()
        self.ingredientDisplayWidget = QWidget()
        self.stepDisplayWidget = QWidget()


        # Create layouts
        self.centralWidgetLayoutH = QHBoxLayout()
        self.displayWidgetLayoutV = QVBoxLayout()
        # inputWidgetLayoutV created dynamically in _createDataInputWidget()
        self.inputWidgetLayoutV.addStretch()
        self.ingredientDisplayWidgetLayoutV = QVBoxLayout()
        self.stepDisplayWidgetLayoutV = QVBoxLayout()

        # Add widgets to layouts
        self.centralWidgetLayoutH.addWidget(self.inputWidget)
        self.centralWidgetLayoutH.addWidget(self.displayWidget)
        self.displayWidgetLayoutV.addWidget(self.ingredientDisplayWidget)
        self.displayWidgetLayoutV.addWidget(self.stepDisplayWidget)
        for i in range(10):
            self.ingredientDisplayWidgetLayoutV.addWidget(QLabel("INGREDIENT"))
        for i in range(5):
            self.stepDisplayWidgetLayoutV.addWidget(QPushButton("STEP"))

        # Set Layouts
        self.centralWidget.setLayout(self.centralWidgetLayoutH)
        self.displayWidget.setLayout(self.displayWidgetLayoutV)
        # inputWidget.setLayout(self.inputWidgetLayoutV) happens dynamically in _createDataInputWidget()
        self.ingredientDisplayWidget.setLayout(self.ingredientDisplayWidgetLayoutV)
        self.stepDisplayWidget.setLayout(self.stepDisplayWidgetLayoutV)

        self.setCentralWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.centralWidget)

        self.ingredientDisplayWidget.setGeometry(600, 100, 1000, 900)


    # Creates the widget where user is going to input data
    def _createDataInputWidget(self) -> Type[QWidget]:
        self.inputWidget = QWidget()
        self.inputWidget.setStyleSheet("background-color: #C7CCDB;")
        self.inputWidgetLayoutV = QVBoxLayout()

        #Create rows of corresponding text, entry and buttons
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Ingredients: ", "Add Ingredient", print))    
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Steps: ", "Add Step", print))
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Notes: ", "Add Note", print))
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Tags: ", "Add Tag", print))
        # testButton = QPushButton("TEST")
        # testButton.clicked.connect(lambda: print("TESTING"))
        # inputWidgetLayoutV.addWidget(testButton)
        self.inputWidget.setLayout(self.inputWidgetLayoutV)
        return self.inputWidget

    # Creates a row with descriptive text, entry line and button
    def _createDataInputRow(self, labelText: str, ButtonText: str, action: Callable) -> Type[QWidget]: 

        dataInputRow = QWidget()
        dataInputRowLayout = QHBoxLayout()
        dataInputRowLayout.addWidget(QLabel(labelText))

        # create line edit
        customLineEdit = QLineEdit()
        customLineEdit.setStyleSheet("background-color:#E1E5EE")
        customLineEdit.returnPressed.connect(lambda: action(customLineEdit.text()))
        dataInputRowLayout.addWidget(customLineEdit)

        # create button
        customButton = QPushButton(ButtonText)
        customButton.clicked.connect(lambda: action(buttonLineEditPairs[customButton].text()))
        customButton.setStyleSheet("background-color:#767B91; color:#E1E5EE")
        dataInputRowLayout.addWidget(customButton)
        
        dataInputRow.setLayout(dataInputRowLayout)

        # pair the buttons to the corresponding line edits
        buttonLineEditPairs[customButton]=customLineEdit
        return dataInputRow



       




if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

# see about making colors constants
# add type hints
# document

