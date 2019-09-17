from PyQt4 import uic,QtGui
import pyodbc

( Ui_People_Staff_View, QDialog ) = uic.loadUiType( 'People_Staff_View.ui' )

class People_Staff_View ( QDialog ):
    """People_Staff_View inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Staff_View()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    
    def RefreshStaff(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Staff")
        records = point.fetchall()
        link.close()
        count = 0
        for record in records:
            #not checked
            self.ui.StaffView.removeRow(count)
            self.ui.StaffView.insertRow(count)
            self.ui.StaffStaffView.setItem(count,0,QtGui.QTableWidgetItem(str(record[0])))
            self.ui.StaffView.setItem(count,1,QtGui.QTableWidgetItem(str(record[1])))
            self.ui.StaffView.setItem(count,2,QtGui.QTableWidgetItem(str(record[2])))
            self.ui.StaffView.setItem(count,3,QtGui.QTableWidgetItem(str(record[3])))
            self.ui.StaffView.setItem(count,4,QtGui.QTableWidgetItem(str(record[4])))
            count = count + 1

    def BackButton(self):
        self.close()
