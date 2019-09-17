from PyQt4 import uic, QtGui
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap
import Music_Podcasts_Add
import Music_Podcasts_View

( Ui_Music_Podcasts_Main, QDialog ) = uic.loadUiType( 'Music_Podcasts_Main.ui' )

class Music_Podcasts_Main ( QDialog ):
    """Music_Podcasts_Main inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Podcasts_Main()
        self.ui.setupUi( self )
        self.ui.PodcastMenu_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png"))

    def __del__ ( self ):
        self.ui = None

    def AddPodcastButton(self):
        self.PodcastsAddForm = Music_Podcasts_Add.Music_Podcasts_Add()
        self.PodcastsAddForm.exec_()
    
    def ViewPodcastsButton(self):
        self.PodcastsViewForm = Music_Podcasts_View.Music_Podcasts_View()
        self.PodcastsViewForm.exec_()
    
    def BackButton(self):
        self.close()