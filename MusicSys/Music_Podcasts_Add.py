from PyQt4 import uic,QtGui
import pyodbc
from Validation import Validation

( Ui_Music_Podcasts_Add, QDialog ) = uic.loadUiType( 'Music_Podcasts_Add.ui' )

class Music_Podcasts_Add ( QDialog ):
    """Music_Podcasts_Add inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Podcasts_Add()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def AddPodcast(self):
        self.ui.AddPodcast_KeyValidation.setText("")
        self.ui.AddPodcast_CommentsValidation.setText("")
        
        self.ui.AddPodcast_KeyValidation.setText(Validation.PresenceCheck(self.ui.AddPodcast_KeyWordsBox.text()))
        self.ui.AddPodcast_CommentsValidation.setText(Validation.LengthCheckXL(self.ui.AddPodcast_CommentsBox.text()))
        
        if self.ui.AddPodcast_KeyValidation.text() == "" and self.ui.AddPodcast_CommentsValidation.text() == "":
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=H:\\Subjects\A2 Computing\CG4\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("insert into Podcasts(Podcast_ID,KeyWords,Comments)values(?,?,?)",self.ui.AddPodcast_NumberBox.text(),self.ui.AddPodcast_KeyWordsBox.text(),self.ui.AddPodcast_CommentsBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Podcast Saved.')
            self.close()
    
    def CancelButton(self):
        self.close()