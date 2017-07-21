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
        if fileName:
            print(fileName)
            
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;xml (*.xml)", options=options)
        if fileName:
            print(fileName)
            
class Projectors():
    
    def __init__(self,ip):
        self.ip = ip
        
        
    def openConnection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con = s.connect((self,80))
    
        def Close(self,con):
            con.close()
        
    
    
    