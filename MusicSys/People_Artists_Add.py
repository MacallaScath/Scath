from PyQt4 import uic,QtGui
import pyodbc
from Validation import Validation

( Ui_People_Artists_Add, QDialog ) = uic.loadUiType( 'People_Artists_Add.ui' )

class People_Artists_Add ( QDialog ):
    """People_Artists_Add inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Artists_Add()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def AddArtist(self):
        self.ui.AddArtist_TitleValidation.setText("")
        self.ui.AddArtist_KeyValidation.setText("")
        self.ui.AddArtist_CommentsValidation.setText("")
        self.ui.AddArtist_CodeValidation.setText("")
        
        self.ui.AddArtist_TitleValidation.setText(Validation.PresenceCheck(self.ui.AddArtist_TitleBox.text()))
        self.ui.AddArtist_KeyValidation.setText(Validation.PresenceCheck(self.ui.AddArtist_KeyWordsBox.text()))
        self.ui.AddArtist_CommentsValidation.setText(Validation.LengthCheckXL(self.ui.AddArtist_CommentsBox.text()))
        self.ui.AddArtist_CodeValidation.setText(Validation.CodeCheck(self.ui.AddArtist_CodeBox.text()))
        
        if self.ui.AddArtist_TitleValidation.text() == "" and self.ui.AddArtist_KeyValidation.text() == "" and self.ui.AddArtist_CommentsValidation.text() == "" and self.ui.AddArtist_CodeValidation.text() == "":
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("insert into Artists(Artist_ID,ArtistName,Published,KeyWords,Comments)values(?,?,?,?,?)",self.ui.AddArtist_NumberBox.text(),self.ui.AddArtist_TitleBox.text(),self.ui.AddArtist_DateBox.text(),self.ui.AddArtist_KeyWordsBox.text(),self.ui.AddArtist_CommentsBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Artist Saved.')
            self.close()

    def BackButton(self):
        self.close()