from PyQt4 import uic,QtGui
import pyodbc
from Validation import Validation

( Ui_People_Email_Add, QDialog ) = uic.loadUiType( 'People_Email_Add.ui' )

class People_Email_Add ( QDialog ):
    """People_Email_Add inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Email_Add()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def AddEmail(self):
        """VALIDATIONself.ui.AddAlbum_TitleValidation.setText("")
        self.ui.AddAlbum_KeyValidation.setText("")
        self.ui.AddAlbum_CommentsValidation.setText("")
        self.ui.AddAlbum_CodeValidation.setText("")
        
        self.ui.AddAlbum_TitleValidation.setText(Validation.PresenceCheck(self.ui.AddAlbum_TitleBox.text()))
        self.ui.AddAlbum_KeyValidation.setText(Validation.PresenceCheck(self.ui.AddAlbum_KeyWordsBox.text()))
        self.ui.AddAlbum_CommentsValidation.setText(Validation.LengthCheckXL(self.ui.AddAlbum_CommentsBox.text()))
        self.ui.AddAlbum_CodeValidation.setText(Validation.CodeCheck(self.ui.AddAlbum_CodeBox.text()))"""
        
        #VALIDATIONif self.ui.AddAlbum_TitleValidation.text() == "" and self.ui.AddAlbum_KeyValidation.text() == "" and self.ui.AddAlbum_CommentsValidation.text() == "" and self.ui.AddAlbum_CodeValidation.text() == "":
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("insert into Emails(FirstName,Surname,Email)values(?,?,?)",self.ui.AddEmail_FirstNameBox.text(),self.ui.AddEmail_SurnameBox.text(),self.ui.AddEmail_EmailBox.text())
        link.commit()
        QtGui.QMessageBox.about(self,' ','Email Saved.')
        self.close()

    def BackButton(self):
        self.close()