from PyQt4 import uic, QtGui
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
import Music_Albums_Main
import Music_Songs_Main
import Music_Podcasts_Main

( Ui_Music_Menu, QDialog ) = uic.loadUiType( 'Music_Menu.ui' )

class Music_Menu ( QDialog ):
    """Music_Menu inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Menu()
        self.ui.setupUi( self )
        self.ui.Music_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png"))

    def __del__ ( self ):
        self.ui = None

    def AlbumsMainButton(self):
        self.AlbumsMainForm = Music_Albums_Main.Music_Albums_Main()
        self.AlbumsMainForm.exec_()
    
    def SongsMainButton(self):
        self.SongsMainForm = Music_Songs_Main.Music_Songs_Main()
        self.SongsMainForm.exec_()
    
    def PodcastsMainButton(self):
        self.PodcastsMainForm = Music_Podcasts_Main.Music_Podcasts_Main()
        self.PodcastsMainForm.exec_()
    
    def BackButton(self):
        self.close()