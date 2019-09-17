from PyQt4 import uic,QtGui
import pyodbc
from Validation import Validation

( Ui_Merchandise_Add, QDialog ) = uic.loadUiType( 'Merchandise_Add.ui' )

class Merchandise_Add ( QDialog ):
    """Merchandise_Add inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Merchandise_Add()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def AddMerchandise(self):
        self.ui.AddMerchandise_TitleValidation.setText("")
        self.ui.AddMerchandise_KeyValidation.setText("")
        self.ui.AddMerchandise_CommentsValidation.setText("")
        self.ui.AddMerchandise_CodeValidation.setText("")
        
        self.ui.AddMerchandise_TitleValidation.setText(Validation.PresenceCheck(self.ui.AddMerchandise_TitleBox.text()))
        self.ui.AddMerchandise_KeyValidation.setText(Validation.PresenceCheck(self.ui.AddMerchandise_KeyWordsBox.text()))
        self.ui.AddMerchandise_CommentsValidation.setText(Validation.LengthCheckXL(self.ui.AddMerchandise_CommentsBox.text()))
        self.ui.AddMerchandise_CodeValidation.setText(Validation.CodeCheck(self.ui.AddMerchandise_CodeBox.text()))
        
        if self.ui.AddMerchandise_TitleValidation.text() == "" and self.ui.AddMerchandise_KeyValidation.text() == "" and self.ui.AddMerchandise_CommentsValidation.text() == "" and self.ui.AddMerchandise_CodeValidation.text() == "":
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("insert into Merchandise(Merchandise_ID,MerchandiseName,Published,KeyWords,Comments)values(?,?,?,?,?)",self.ui.AddMerchandise_NumberBox.text(),self.ui.AddMerchandise_TitleBox.text(),self.ui.AddMerchandise_DateBox.text(),self.ui.AddMerchandise_KeyWordsBox.text(),self.ui.AddMerchandise_CommentsBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','New Item Saved.')
            self.close()

    def BackButton(self):
        self.close()