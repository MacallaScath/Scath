from PyQt4 import uic,QtGui
import pyodbc

( Ui_Music_Albums_View, QDialog ) = uic.loadUiType( 'Music_Albums_View.ui' )

class Music_Albums_View ( QDialog ):
    """Music_Albums_View inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Albums_View()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def RefreshAlbums(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Albums")
        records = point.fetchall()
        link.close()
        count = 0
        for record in records:
            self.ui.AlbumsView.removeRow(count)
            self.ui.AlbumsView.insertRow(count)
            self.ui.AlbumsView.setItem(count,0,QtGui.QTableWidgetItem(str(record[0])))
            self.ui.AlbumsView.setItem(count,1,QtGui.QTableWidgetItem(str(record[1])))
            self.ui.AlbumsView.setItem(count,2,QtGui.QTableWidgetItem(str(record[2])))
            self.ui.AlbumsView.setItem(count,3,QtGui.QTableWidgetItem(str(record[3])))
            self.ui.AlbumsView.setItem(count,4,QtGui.QTableWidgetItem(str(record[4])))
            count = count + 1

    def BackButton(self):
        self.close()