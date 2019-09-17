from PyQt4 import uic, QtGui
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
import Merchandise_Add
import Merchandise_View
import Merchandise_Search
import Merchandise_Sales

( Ui_Merchandise_Menu, QDialog ) = uic.loadUiType( 'Merchandise_Menu.ui' )

class Merchandise_Menu ( QDialog ):
    """Merchandise_Menu inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Merchandise_Menu()
        self.ui.setupUi( self )
        self.ui.Merchandise_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png"))

    def __del__ ( self ):
        self.ui = None

    def AddMerchandise(self):
        self.AddMerchandiseForm = Merchandise_Add.Merchandise_Add()
        self.AddMerchandiseForm.exec_()
    
    def ViewMerchandise(self):
        self.ViewMerchandiseForm = Merchandise_View.Merchandise_View()
        self.ViewMerchandiseForm.exec_()
    
    def SearchMerchandise(self):
        self.SearchMerchandiseForm = Merchandise_Search.Merchandise_Search()
        self.SearchMerchandiseForm.exec_()
    
    def MerchandiseSales(self):
        self.MerchandiseSalesForm = Merchandise_Sales.Merchandise_Sales()
        self.MerchandiseSalesForm.exec_()

    def BackButton(self):
        self.close()