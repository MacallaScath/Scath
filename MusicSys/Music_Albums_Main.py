from PyQt4 import uic, QtGui
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
import Music_Albums_Add
import Music_Albums_View
import Music_Albums_Search
import Music_Albums_Sales

( Ui_Music_Albums_Main, QDialog ) = uic.loadUiType( 'Music_Albums_Main.ui' )

class Music_Albums_Main ( QDialog ):
    """Music_Albums_Main inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Albums_Main()
        self.ui.setupUi( self )
        self.ui.AlbumMenu_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png"))

    def __del__ ( self ):
        self.ui = None

    def AddAlbumButton(self):
        self.AlbumsAddForm = Music_Albums_Add.Music_Albums_Add()
        self.AlbumsAddForm.exec_()
    
    def ViewAlbumsButton(self):
        self.AlbumsViewForm = Music_Albums_View.Music_Albums_View()
        self.AlbumsViewForm.exec_()
    
    def SearchAlbumsButton(self):
        self.AlbumsSearchForm = Music_Albums_Search.Music_Albums_Search()
        self.AlbumsSearchForm.exec_()
    
    def AlbumSalesButton(self):
        self.AlbumSalesForm = Music_Albums_Sales.Music_Albums_Sales()
        self.AlbumSalesForm.exec_()
    
    def BackButton(self):
        self.close()