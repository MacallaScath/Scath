from PyQt4 import uic,QtGui
import pyodbc

( Ui_People_Artists_View, QDialog ) = uic.loadUiType( 'People_Artists_View.ui' )

class People_Artists_View ( QDialog ):
    """People_Artists_View inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Artists_View()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def RefreshArtists(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Artists")
        records = point.fetchall()
        link.close()
        count = 0
        for record in records:
            #not checked
            self.ui.ArtistsView.removeRow(count)
            self.ui.ArtistsView.insertRow(count)
            self.ui.ArtistsView.setItem(count,0,QtGui.QTableWidgetItem(str(record[0])))
            self.ui.ArtistsView.setItem(count,1,QtGui.QTableWidgetItem(str(record[1])))
            self.ui.ArtistsView.setItem(count,2,QtGui.QTableWidgetItem(str(record[2])))
            self.ui.ArtistsView.setItem(count,3,QtGui.QTableWidgetItem(str(record[3])))
            self.ui.ArtistsView.setItem(count,4,QtGui.QTableWidgetItem(str(record[4])))
            count = count + 1

    def BackButton(self):
        self.close()