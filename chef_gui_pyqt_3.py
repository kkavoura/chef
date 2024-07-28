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
    QScrollArea,
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, pyqtSignal
from manager import Manager
from typing import Callable, Type

guiManager = Manager()
buttonLineEditPairs = {}


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        #REMOVE THIS
        guiManager.initialize_recipe()

        menubar = self.menuBar()
        recipeMenu = menubar.addMenu("Recipe")
        newRecipeAction = QAction("New Recipe", self)
        newRecipeAction.triggered.connect(guiManager.initialize_recipe)
        recipeMenu.addAction(newRecipeAction)



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

        saveButton = QPushButton("Save Recipe")
        self.inputWidgetLayoutV.addWidget(saveButton)
        saveButton.clicked.connect(guiManager.print_recipe)

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
        print(guiManager.check_duplicate_ingredient(ingredientText))
        if guiManager.check_duplicate_ingredient(ingredientText):
            return
        guiManager.add_ingredient(ingredientText)
        label = self._createLabel(ingredientText, self.ingredientDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.ingredientDisplayWidgetLayoutV, label))
        label.clicked.connect(lambda: guiManager.remove_ingredient(ingredientText))

    # Add a step - Take input, send input to gui manager, display input
    def _addStep(self, stepText:str) -> None:
        currentStep = guiManager.add_step(stepText)
        label = self._createLabel(self._createStepLabelText(stepText), self.stepDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.stepDisplayWidgetLayoutV, label))
        label.clicked.connect(lambda: guiManager.remove_step(currentStep))
        label.clicked.connect(lambda: self.updateStepNumberOnLabel())

    # Iterates through step labels in stepDisplayWidget and updates the step counter on each
    def updateStepNumberOnLabel(self) -> None:

        for i in range(self.stepDisplayWidgetLayoutV.count()):
            widget = self.stepDisplayWidgetLayoutV.itemAt(i).widget()
            if widget is not None:
                if isinstance(widget, QLabel):
                    widgetText = widget.text()
                    textNumber = widgetText.split(".")[0]
                    widget.setText(str(i+1)+". "+widgetText.split(". ")[1])

    def _createStepLabelText(self, text:str)->str:
        myString = str(guiManager.get_current_step_number()) + ". " + text
        print("Creating Step Label text with input " + text + " and number " + str(guiManager.get_current_step_number()))
        return myString

    # Add a note - Take input, send input to gui manager, display input
    def _addNote(self, noteText:str) -> None:
        guiManager.add_note(noteText)
        label = self._createLabel(noteText, self.noteDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.noteDisplayWidgetLayoutV, label))
        label.clicked.connect(lambda: guiManager.remove_note(noteText))

    # Add a tag - Take input, send input to gui manager, display input
    def _addTag(self, tagText:str) -> None:
        if guiManager.check_duplicate_tag(tagText):
            return
        guiManager.add_tag(tagText)
        label = self._createLabel(tagText, self.tagDisplayWidget)
        label.clicked.connect(lambda: self.removeLabel(self.tagDisplayWidgetLayoutV, label))
        label.clicked.connect(lambda: guiManager.remove_tag(tagText))

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
# make labels drag and drop

# IMPORTANT: remove step when label is removed
# prevent duplicates in tag, ingredient, step no (data structure?)
# remove generated venv files, do requirements.txt


# getcurrentstepnumber - > getlaststepnumber

# it won't create duplicates because of dictionary but it does still create duplicate label
# trim whitespace
