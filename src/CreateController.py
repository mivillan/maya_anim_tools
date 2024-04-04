print("hello!!")
import maya.cmds as mc

from PySide2.QtWidgets import QWidget  #all outlines, window, graph editors are widgets

class CreateControllerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create IKFK Limb")

controllerWidget = CreateControllerWidget()
controllerWidget.show()












#send to maya through Alt+Shift+M, will run through MEL
# use "commandPort -name "localhost:7001" -sourceType "mel";
#to open file, go to search bar and type "CMD". Once prompted, type "code ." into the bar for it to run visual studio. 