
import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QLabel, QDesktopWidget,QLineEdit,QWidget, QFileDialog, qApp,QMessageBox, QAction, QPushButton,QInputDialog
from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import WA_DeleteOnClose
from Projector import *
'''
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal,pyqtSlot
from PyQt5.QtCore  import QObject
from PyQt5.Qt import QSize
'''
#newcommit


class UserInterface(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        app.setStyleSheet('QMainWindow{background-color: black;border: 1px solid black;}')

     


    def initUI(self):
        
   
    

    #Menu Bar ----------------------------------
        #nameing the exit action and assigning an image
        OpenAction= QAction('&Open File',self)
       # AddAction= QAction('&Add Projector',handleNewWindow.nameBox,handleNewWindow.ipBox)
        SaveAction= QAction('&Save File',self)
        ConAction = QAction(QIcon('Assets/ToolBar/Images/Cat5.png'), '&Connection', self)
        LampAction = QAction(QIcon('Assets/ToolBar/Images/Bulb.png'), '&Lamp', self)
        ShutterAction = QAction(QIcon('Assets/ToolBar/Images/Shutter.png'), '&Shutter', self) 
        TempAction = QAction(QIcon('Assets/ToolBar/Images/Temp.png'), '&Temp', self)
        OsdAction = QAction(QIcon('Assets/ToolBar/Images/OSD.png'), '&OSD', self)
        AddProjector = QAction(QIcon('Assets/ToolBar/Images/Plus.png'), '&Add Projector', self)
        #q action allows us to use a keyboard shortcut
        OpenAction.setShortcut('Ctrl+O')
        SaveAction.setShortcut('Ctrl+S')
        AddProjector.setShortcut('Ctrl+Alt+A')      
        ConAction.setShortcut('Ctrl+Alt+N')
        LampAction.setShortcut('Ctrl+Alt+Shift+Del')
        ShutterAction.setShortcut('Ctrl+Alt+S')
        TempAction.setShortcut('Ctrl+Alt+T')
        OsdAction.setShortcut('Ctrl+Alt+O')
        #displays in the status bar what you are hovering over
        OpenAction.setStatusTip('Open File')
        AddProjector.setStatusTip('Add Projector')
        SaveAction.setStatusTip('Save File')
        ConAction.setStatusTip('Connection')
        LampAction.setStatusTip('Lamp')
        ShutterAction.setStatusTip('Shutter')
        TempAction.setStatusTip(' Temprature')
        OsdAction.setStatusTip('Osd')
        #connecting the action .quit which terminates the application
        #------fix the crash on open and save file
        OpenAction.triggered.connect(file.openFileNameDialog)
        SaveAction.triggered.connect(file.saveFileDialog)
        AddProjector.triggered.connect(file.handleNewWindow)
        ConAction.triggered.connect(qApp.quit)
        LampAction.triggered.connect(qApp.quit)
        ShutterAction.triggered.connect(qApp.quit)
        TempAction.triggered.connect(qApp.quit)
        OsdAction.triggered.connect(qApp.quit)
    #Menu Bar ----------------------------------

        self.toolbar = self.addToolBar('CONTROL')
        self.toolbar.addAction(AddProjector)
        self.toolbar.addAction(ConAction)
        self.toolbar.addAction(LampAction)
        self.toolbar.addAction(ShutterAction)
        self.toolbar.addAction(TempAction)
        self.toolbar.addAction(OsdAction)

        
       
       
        
        #The menuBar() method creates a menubar.
        menubar = self.menuBar()
        #append the menubar with a menu
        Menu = menubar.addMenu('&File')
        scan = menubar.addMenu('&Projectors')
        Help = menubar.addMenu("&Help")
        #Add the Exit action to the menu item
        Menu.addAction(OpenAction)
        Menu.addAction(SaveAction)
        scan.addAction(TempAction)
        Help.addAction(LampAction)


        
 
      
        #The first two parameters are the x and y
        sizeObject = QDesktopWidget().screenGeometry(-1)
        self.statusBar().setStyleSheet("color: white");   
        self.statusBar().showMessage('Ready')
        self.setGeometry(sizeObject.width()/9, sizeObject.width()/16, sizeObject.width()/1.2, sizeObject.height()/1.2)
        self.setWindowTitle('MonTools')
        self.setWindowIcon(QIcon("Assets/ToolBar/Images/Cat5.png"))        
    
        self.show()
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = UserInterface()
    sys.exit(app.exec_()) 