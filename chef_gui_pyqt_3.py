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

from PyQt6.QtCore import Qt, pyqtSignal
from manager import Manager
from typing import Callable, Type

guiManager = Manager()
buttonLineEditPairs = {}


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        # Create widgets
        self.centralWidget = QWidget()
        self.inputWidget = self._createDataInputWidget()
        self.ingredientScrollArea = QScrollArea()
        self.stepScrollArea = QScrollArea()
        self.noteScrollArea = QScrollArea()
        self.tagScrollArea = QScrollArea()
        self.displayWidget = QWidget()
        self.ingredientDisplayWidget = QGroupBox("Ingredients")
        self.stepDisplayWidget = QGroupBox("Steps")
        self.noteDisplayWidget = QGroupBox("Notes")
        self.tagDisplayWidget = QGroupBox("Tags")


        # Create layouts
        self.centralWidgetLayoutH = QHBoxLayout()
        self.displayWidgetLayoutV = QVBoxLayout()
        # inputWidgetLayoutV created dynamically in _createDataInputWidget()
        self.inputWidgetLayoutV.addStretch()
        self.ingredientDisplayWidgetLayoutV = QVBoxLayout()
        self.stepDisplayWidgetLayoutV = QVBoxLayout()
        self.noteDisplayWidgetLayoutV = QVBoxLayout()
        self.tagDisplayWidgetLayoutV = QVBoxLayout()

        # Add widgets to layouts
        self.centralWidgetLayoutH.addWidget(self.inputWidget)
        self.centralWidgetLayoutH.addWidget(self.displayWidget)
        self.displayWidgetLayoutV.addWidget(self.ingredientScrollArea, stretch=4)
        self.displayWidgetLayoutV.addWidget(self.stepScrollArea, stretch=3)
        self.displayWidgetLayoutV.addWidget(self.noteScrollArea, stretch=2)
        self.displayWidgetLayoutV.addWidget(self.tagScrollArea, stretch=2)



        # Set Layouts
        self.centralWidget.setLayout(self.centralWidgetLayoutH)
        self.displayWidget.setLayout(self.displayWidgetLayoutV)
        # inputWidget.setLayout(self.inputWidgetLayoutV) happens dynamically in _createDataInputWidget()
        self.ingredientDisplayWidget.setLayout(self.ingredientDisplayWidgetLayoutV)
        self.stepDisplayWidget.setLayout(self.stepDisplayWidgetLayoutV)
        self.noteDisplayWidget.setLayout(self.noteDisplayWidgetLayoutV)
        self.tagDisplayWidget.setLayout(self.tagDisplayWidgetLayoutV)

        self.setCentralWidget(self.centralWidget)

        self.ingredientScrollArea.setWidgetResizable(True)
        self.ingredientScrollArea.setWidget(self.ingredientDisplayWidget)
        self.stepScrollArea.setWidgetResizable(True)
        self.stepScrollArea.setWidget(self.stepDisplayWidget)
        self.noteScrollArea.setWidgetResizable(True)
        self.noteScrollArea.setWidget(self.noteDisplayWidget)
        self.tagScrollArea.setWidgetResizable(True)
        self.tagScrollArea.setWidget(self.tagDisplayWidget)
        
        self.setGeometry(150, 300, 800, 500)


    # Creates the widget where user is going to input data
    def _createDataInputWidget(self) -> Type[QWidget]:
        self.inputWidget = QWidget()
        self.inputWidget.setStyleSheet("background-color: #C7CCDB;")
        self.inputWidgetLayoutV = QVBoxLayout()

        #Create rows of corresponding text, entry and buttons
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Ingredients: ", "Add Ingredient", self._addIngredient))    
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Steps: ", "Add Step", self._addStep))
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Notes: ", "Add Note", self._addNote))
        self.inputWidgetLayoutV.addWidget(self._createDataInputRow("Tags: ", "Add Tag", self._addTag))
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
        customLineEdit.returnPressed.connect(lambda: customLineEdit.setText(""))
        dataInputRowLayout.addWidget(customLineEdit)

        # create button
        customButton = QPushButton(ButtonText)
        customButton.clicked.connect(lambda: action(buttonLineEditPairs[customButton].text()))
        customButton.clicked.connect(lambda: buttonLineEditPairs[customButton].setText(""))
        customButton.setStyleSheet("background-color:#767B91; color:#E1E5EE")
        dataInputRowLayout.addWidget(customButton)
        
        dataInputRow.setLayout(dataInputRowLayout)

        # pair the buttons to the corresponding line edits
        buttonLineEditPairs[customButton]=customLineEdit
        return dataInputRow

    # Add ingredient - Take input, send input to gui manager, display input
    def _addIngredient(self, ingredientText:str) -> None:
        guiManager.add_ingredient(ingredientText)
        label = self._createLabel(ingredientText, self.ingredientDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.ingredientDisplayWidgetLayoutV, label))

    # Add a step - Take input, send input to gui manager, display input
    def _addStep(self, stepText:str) -> None:
        thisStep = guiManager.create_new_step(stepText)
        # label = self._createLabel(str(thisStep.counter)+". "+stepText, self.stepDisplayWidget)
        label = self._createLabel(self._createStepLabelText(stepText), self.stepDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.stepDisplayWidgetLayoutV, label))
        txt = self._createStepLabelText(stepText)
######################################################### RESUME HERE
###     create label text is passing around a method and not a str
    # Creates text for step label
    def _createStepLabelText(self, text:str)->str:
        myString = str(self._getStepNumber()) + ". " + text
        print("Creating Step Label text with input " + text + " and number " + str(self._getStepNumber()))
        return myString

    # Returns the current step number
    def _getStepNumber(self):
        stepNo = guiManager.get_current_step_number()
        return stepNo

    # Add a note - Take input, send input to gui manager, display input
    def _addNote(self, noteText:str) -> None:
        guiManager.create_new_note(noteText)
        label = self._createLabel(noteText, self.noteDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.noteDisplayWidgetLayoutV, label))

    # Add a tag - Take input, send input to gui manager, display input
    def _addTag(self, tagText:str) -> None:
        guiManager.create_new_tag(tagText)
        label = self._createLabel(tagText, self.tagDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.tagDisplayWidgetLayoutV, label))

    # Adds a label with given text to target widget
    def _createLabel(self, text:str, targetWidget:Type[QWidget]) -> Type[QLabel]:
        newLabel = ClickableLabel(text)
        newLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        newLabelSizeHint = newLabel.sizeHint()
        newLabel.setFixedSize(newLabelSizeHint.width() + 20, 30)
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
        targetWidget.layout().addWidget(newLabel)
        targetWidget.setLayout(targetWidget.layout())
        self.moveScrollBarToBottom(self.ingredientScrollArea)
        return newLabel

    # Removes a label from a layout
    def removeLabel(self, layout, label):
        layout.removeWidget(label)
        label.deleteLater()

    # Given a target ScrollArea, moves the vertical scrollbar to the bottom
    def moveScrollBarToBottom(self, currentScrollArea):
        scrollBar = currentScrollArea.verticalScrollBar()
        scrollBar.rangeChanged.connect(lambda: scrollBar.setValue(scrollBar.maximum()))


# Custom QLabel subclass that has a click event handler
class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

# see about making colors constants
# add type hints
# document
# consider how functions are passed around with button line edit pairing
# validate input
# actually remove ingredients from object when label is removed
