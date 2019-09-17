from PyQt4 import uic, QtGui
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
import People_Staff_View
import People_Staff_Add

( Ui_People_Staff_Menu, QDialog ) = uic.loadUiType( 'People_Staff_Menu.ui' )

class People_Staff_Menu ( QDialog ):
    """People_Staff_Menu inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Staff_Menu()
        self.ui.setupUi( self )
        self.ui.StaffMenu_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png"))

    def __del__ ( self ):
        self.ui = None

    def ViewStaffButton(self):
        self.StaffViewForm = People_Staff_View.People_Staff_View()
        self.StaffViewForm.exec_()
    
    def AddStaffButton(self):
        self.StaffAddForm = People_Staff_Add.People_Staff_Add()
        self.StaffAddForm.exec_()
        
    def BackButton(self):
        self.close()