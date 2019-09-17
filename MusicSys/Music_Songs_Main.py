from PyQt4 import uic, QtGui
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
import Music_Songs_Add
import Music_Songs_View
import Music_Songs_Search
import Music_Songs_Sales

( Ui_Music_Songs_Main, QDialog ) = uic.loadUiType( 'Music_Songs_Main.ui' )

class Music_Songs_Main ( QDialog ):
    """Music_Songs_Main inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Songs_Main()
        self.ui.setupUi( self )
        self.ui.SongMenu_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png"))

    def __del__ ( self ):
        self.ui = None

    def AddSongButton(self):
        self.SongsAddForm = Music_Songs_Add.Music_Songs_Add()
        self.SongsAddForm.exec_()
    
    def ViewSongsButton(self):
        self.SongsViewForm = Music_Songs_View.Music_Songs_View()
        self.SongsViewForm.exec_()
    
    def SearchSongsButton(self):
        self.SongsSearchForm = Music_Songs_Search.Music_Songs_Search()
        self.SongsSearchForm.exec_()
    
    def SongSalesButton(self):
        self.SongSalesForm = Music_Songs_Sales.Music_Songs_Sales()
        self.SongSalesForm.exec_()
    
    def BackButton(self):
        self.close()