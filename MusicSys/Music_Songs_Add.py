from PyQt4 import uic,QtGui
import pyodbc
from Validation import Validation

( Ui_Music_Songs_Add, QDialog ) = uic.loadUiType( 'Music_Songs_Add.ui' )

class Music_Songs_Add ( QDialog ):
    """Music_Songs_Add inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Songs_Add()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
        
    def AddSong(self):
        self.ui.AddSong_TitleValidation.setText("")
        self.ui.AddSong_KeyValidation.setText("")
        self.ui.AddSong_CommentsValidation.setText("")
        self.ui.AddSong_CodeValidation.setText("")
        
        self.ui.AddSong_TitleValidation.setText(Validation.PresenceCheck(self.ui.AddSong_TitleBox.text()))
        self.ui.AddSong_KeyValidation.setText(Validation.PresenceCheck(self.ui.AddSong_KeyWordsBox.text()))
        self.ui.AddSong_CommentsValidation.setText(Validation.LengthCheckXL(self.ui.AddSong_CommentsBox.text()))
        self.ui.AddSong_CodeValidation.setText(Validation.CodeCheck(self.ui.AddSong_CodeBox.text()))
        
        if self.ui.AddSong_TitleValidation.text() == "" and self.ui.AddSong_KeyValidation.text() == "" and self.ui.AddSong_CommentsValidation.text() == "" and self.ui.AddSong_CodeValidation.text() == "":
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("insert into Songs(Song_ID,SongName,KeyWords,Comments)values(?,?,?,?)",self.ui.AddSong_NumberBox.text(),self.ui.AddSong_TitleBox.text(),self.ui.AddSong_KeyWordsBox.text(),self.ui.AddSong_CommentsBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Song Saved.')
            self.close()
        
    def CancelButton(self):
        self.close()