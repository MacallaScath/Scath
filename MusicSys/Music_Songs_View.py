from PyQt4 import uic,QtGui
import pyodbc

( Ui_Music_Songs_View, QDialog ) = uic.loadUiType( 'Music_Songs_View.ui' )

class Music_Songs_View ( QDialog ):
    """Music_Songs_View inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Songs_View()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def RefreshSongs(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Songs")
        records = point.fetchall()
        link.close()
        count = 0
        for record in records:
            self.ui.SongsView.removeRow(count)
            self.ui.SongsView.insertRow(count)
            self.ui.SongsView.setItem(count,0,QtGui.QTableWidgetItem(str(record[0])))
            self.ui.SongsView.setItem(count,1,QtGui.QTableWidgetItem(str(record[1])))
            self.ui.SongsView.setItem(count,2,QtGui.QTableWidgetItem(str(record[2])))
            self.ui.SongsView.setItem(count,3,QtGui.QTableWidgetItem(str(record[3])))
            self.ui.SongsView.setItem(count,4,QtGui.QTableWidgetItem(str(record[4])))
            count = count + 1

    def BackButton(self):
        self.close()
        
    