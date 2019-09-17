from PyQt4 import uic, QtGui
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
import People_Staff_Menu
import People_Artists_Menu
import People_Email_Menu

( Ui_People_Menu, QDialog ) = uic.loadUiType( 'People_Menu.ui' )

class People_Menu ( QDialog ):
    """People_Menu inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Menu()
        self.ui.setupUi( self )
        self.ui.People_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png"))

    def __del__ ( self ):
        self.ui = None

    def BackButton(self):
        self.close()
    
    def ArtistsButton(self):
        self.ArtistsMenuForm = People_Artists_Menu.People_Artists_Menu()
        self.ArtistsMenuForm.exec_()
    
    def StaffButton(self):
        self.StaffMenuForm = People_Staff_Menu.People_Staff_Menu()
        self.StaffMenuForm.exec_()
    
    def EmailButton(self):
        self.EmailMenuForm = People_Email_Menu.People_Email_Menu()
        self.EmailMenuForm.exec_()