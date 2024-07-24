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
from functools import partial 
from typing import Callable, Type

guiManager = Manager()
buttonLineEditPairs = {}


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        self.setMinimumSize(600, 400) 
              
        self.vbox = QVBoxLayout()  

        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet("background-color:#CEF7A0; color:#2A324B")

        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle("Chef Main Window")
        self.dataInputWidget = self._createDataInputWidget()
        self.dataDisplayWidget = self._createDataDisplayWidget()

        self.dataDisplayWidgetLayout = self.dataDisplayWidget.findChildren(QVBoxLayout)[0]

        mainWidgetLayout = QHBoxLayout()
        mainWidgetLayout.addWidget(self.dataInputWidget)
        mainWidgetLayout.addWidget(self.dataDisplayWidget)

        self.mainWidget.setLayout(mainWidgetLayout)

        self._createMenu()
        # self._createToolBar()
        # self._createStatusBar()

    # Creates the widget where user is going to input data
    def _createDataInputWidget(self):
        dataInputWidget = QWidget()
        dataInputWidget.setStyleSheet("background-color: #C7CCDB;")
        dataInputLayout = QVBoxLayout()

        #Create rows of corresponding text, entry and buttons
        dataInputLayout.addWidget(self._createDataInputRow("Ingredients: ", "Add Ingredient", self._addIngredient))    
        dataInputLayout.addWidget(self._createDataInputRow("Steps: ", "Add Step", guiManager.create_new_step))
        dataInputLayout.addWidget(self._createDataInputRow("Notes: ", "Add Note", guiManager.create_new_note))
        dataInputLayout.addWidget(self._createDataInputRow("Tags: ", "Add Tag", guiManager.create_new_tag))
        testButton = QPushButton("TEST")
        testButton.clicked.connect(lambda: print("TESTING"))
        dataInputLayout.addWidget(testButton)
        dataInputWidget.setLayout(dataInputLayout)
        return dataInputWidget

    # Handle call to add ingredient - Take input, send input to gui manager, display input
    def _addIngredient(self, ingredientText:str) -> None:
        global dataDisplayWidget
        print("in add ingredient " + ingredientText)
        guiManager.add_ingredient(ingredientText)
        self._createIngredientLabel(ingredientText)

    # Creates a row with descriptive text, entry line and button
    def _createDataInputRow(self, labelText: str, ButtonText: str, action: Callable) -> Type[QWidget]: 

        dataInputRow = QWidget()
        dataInputRowLayout = QHBoxLayout()
        dataInputRowLayout.addWidget(QLabel(labelText))

        #create line edit
        customLineEdit = QLineEdit()
        customLineEdit.setStyleSheet("background-color:#E1E5EE")
        customLineEdit.returnPressed.connect(lambda: action(customLineEdit.text()))
        dataInputRowLayout.addWidget(customLineEdit)

        #create button
        customButton = QPushButton(ButtonText)
        customButton.clicked.connect(lambda: action(buttonLineEditPairs[customButton].text()))
        customButton.setStyleSheet("background-color:#767B91; color:#E1E5EE")
        dataInputRowLayout.addWidget(customButton)
        
        dataInputRow.setLayout(dataInputRowLayout)

        #pair the buttons to the corresponding line edits
        self.pairButtonsWithLineEdits(customButton, customLineEdit)
        return dataInputRow

    # Creates the data display widget
    def _createDataDisplayWidget(self) -> Type[QWidget]:

        dataDisplayWidget = QWidget()
        dataDisplayWidget.setStyleSheet("background-color: #C7CCDB")
        dataDisplayLayout = QVBoxLayout()


        # Create ingredients display
        self.ingredientDisplayWidget = QGroupBox("Ingredients")
        self.ingredientDisplayLayout = QVBoxLayout()

    # reset scroll layout after every label is added?


        self.ingredientDisplayWidget.setLayout(self.ingredientDisplayLayout)

        dataDisplayLayout.addWidget(self.ingredientDisplayWidget)
        dataDisplayWidget.setLayout(dataDisplayLayout)
        
        
        # Create steps display
        self.stepDisplayWidget = QGroupBox("Steps")
        self.stepDisplayLayout = QVBoxLayout()
        dataDisplayLayout.addWidget(self.stepDisplayWidget)

        # Create notes display
        noteDisplayWidget = QGroupBox("Notes")
        noteDisplayLayout = QVBoxLayout()
        dataDisplayLayout.addWidget(noteDisplayWidget)

        #Create tags display
        tagDisplayWidget = QGroupBox("Tags")
        tagDisplayLayout = QVBoxLayout()
        dataDisplayLayout.addWidget(tagDisplayWidget)
        
        # dataDisplayWidget.setLayout(dataDisplayLayout)
        return dataDisplayWidget

    # Adds an ingredient label to the Ingredients Display Widget
    def _createIngredientLabel(self, text:str) -> None:
        newLabel = QLabel(text)
        newLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        newLabel.setMinimumSize(100, 5)
        newLabel.setStyleSheet("""
            QLabel {
                background-color: #CEF7A0;
                color:#2A324B;
                border-style: outset;
                border-width: 2px;
                border-color: #2A324B;
            }
            QLabel:hover{
                background-color:#767B91;
                color:#CEF7A0
            }
        """)
        self.ingredientDisplayLayout.addWidget(newLabel)
        self.ingredientDisplayWidget.setLayout(self.ingredientDisplayLayout)







    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("New Recipe", lambda: print("Adding New Recipe"))
        menu.addAction("Load Recipe", lambda: print("Loading Recipe"))
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("This is the status bar!")
        self.setStatusBar(status)

    def pairButtonsWithLineEdits(self, currentButton:Type[QPushButton], currentLineEdit:Type[QLineEdit]) -> None :
        buttonLineEditPairs[currentButton]=currentLineEdit




if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

# see about making colors constants
# add type hints
# document

