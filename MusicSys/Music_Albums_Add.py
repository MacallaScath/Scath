from PyQt4 import uic,QtGui
import pyodbc
from Validation import Validation
import datetime

( Ui_Music_Albums_Add, QDialog ) = uic.loadUiType( 'Music_Albums_Add.ui' )

class Music_Albums_Add ( QDialog ):
    """Music_Albums_Add inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Albums_Add()
        self.ui.setupUi( self )
        self.ui.AddAlbum_DateBox.setDate(datetime.date.today())

    def __del__ ( self ):
        self.ui = None

    def AddAlbum(self):
        self.ui.AddAlbum_TitleValidation.setText("")
        self.ui.AddAlbum_KeyValidation.setText("")
        self.ui.AddAlbum_CommentsValidation.setText("")
        self.ui.AddAlbum_CodeValidation.setText("")
        
        self.ui.AddAlbum_TitleValidation.setText(Validation.PresenceCheck(self.ui.AddAlbum_TitleBox.text()))
        self.ui.AddAlbum_KeyValidation.setText(Validation.PresenceCheck(self.ui.AddAlbum_KeyWordsBox.text()))
        self.ui.AddAlbum_CommentsValidation.setText(Validation.LengthCheckXL(self.ui.AddAlbum_CommentsBox.text()))
        self.ui.AddAlbum_CodeValidation.setText(Validation.CodeCheck(self.ui.AddAlbum_CodeBox.text()))
        
        if self.ui.AddAlbum_TitleValidation.text() == "" and self.ui.AddAlbum_KeyValidation.text() == "" and self.ui.AddAlbum_CommentsValidation.text() == "" and self.ui.AddAlbum_CodeValidation.text() == "":
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("insert into Albums(Album_ID,AlbumName,Published,KeyWords,Comments)values(?,?,?,?,?)",self.ui.AddAlbum_NumberBox.text(),self.ui.AddAlbum_TitleBox.text(),self.ui.AddAlbum_DateBox.text(),self.ui.AddAlbum_KeyWordsBox.text(),self.ui.AddAlbum_CommentsBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Album Saved.')
            self.close()

    def CancelButton(self):
        self.close()