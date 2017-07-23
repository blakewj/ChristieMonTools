import socket
from PyQt5.QtWidgets import QFileDialog


class file():
    def __init__(self):
        super().__init__()
        #self.FileManager()
    
    def FileManager(self,name,ip):
        NewFile = []
        CurrentFile = NewFile.append(name,ip)
        
        return CurrentFile
        
    def saveFileDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;xml Files (*.xml)", options=options)
        if fileNsame:
            print(fileName)
            
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;xml (*.xml)", options=options)
        if fileName:
            print(fileName)
            
    def handleNewWindow(self):
        window = QMainWindow(self)       
        # window.setAttribute(Qt.WA_DeleteOnClose)
        window.setWindowTitle(self.tr('Add Projector'))
        #window.setGeometry(250,250,500,500)
        # Create textbox
        self.ipBox = QLineEdit()
        self.nameBox = QLineEdit()
        
        self.ipBox.resize(400,40)
        self.nameBox.resize(400,40)
        window.setStyleSheet('QMainWindow{background-color: lack;black: 1px solid black;}')
        button = QPushButton("Add Projector") #create button
        
        CentralWidget = QWidget() # create an empty widget
        CentralWidgetLayout = QHBoxLayout() # create a layout
        CentralWidgetLayout.addWidget(button) # add your button to the layout
        CentralWidgetLayout.addWidget(self.ipBox) # add your button to the layout
        CentralWidgetLayout.addWidget(self.nameBox) # add your button to the layout
        CentralWidget.setLayout(CentralWidgetLayout) # assign your layout to the empty widget
        window.setCentralWidget(CentralWidget) #make the assigned widget CentralWidget
        window.resize(450, 100)
        window.show()
        
        return self.ipBox , self.nameBox
    
    def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        
        if ok:
            self.le.setText(str(text))
            
class Projectors():
    
    def __init__(self,ip):
        self.ip = ip
        
        
    def openConnection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con = s.connect((self,80))
    
        def Close(self,con):
            con.close()
        
    
    
    