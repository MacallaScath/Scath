from PyQt4 import uic,QtGui
import pyodbc

( Ui_Merchandise_View, QDialog ) = uic.loadUiType( 'Merchandise_View.ui' )

class Merchandise_View ( QDialog ):
    """Merchandise_View inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Merchandise_View()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def RefreshMerchandise(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Merchandise")
        records = point.fetchall()
        link.close()
        count = 0
        for record in records:
            self.ui.MerchandiseView.removeRow(count)
            self.ui.MerchandiseView.insertRow(count)
            self.ui.MerchandiseView.setItem(count,0,QtGui.QTableWidgetItem(str(record[0])))
            self.ui.MerchandiseView.setItem(count,1,QtGui.QTableWidgetItem(str(record[1])))
            self.ui.MerchandiseView.setItem(count,2,QtGui.QTableWidgetItem(str(record[2])))
            self.ui.MerchandiseView.setItem(count,3,QtGui.QTableWidgetItem(str(record[3])))
            self.ui.MerchandiseView.setItem(count,4,QtGui.QTableWidgetItem(str(record[4])))
            count = count + 1
    
    def BackButton(self):
        self.close()