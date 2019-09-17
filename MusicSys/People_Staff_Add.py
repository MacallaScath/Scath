from PyQt4 import uic,QtGui
import pyodbc
from Validation import Validation

( Ui_People_Staff_Add, QDialog ) = uic.loadUiType( 'People_Staff_Add.ui' )

class People_Staff_Add ( QDialog ):
    """People_Staff_Add inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Staff_Add()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def AddStaff(self):
        self.ui.AddStaff_TitleValidation.setText("")
        self.ui.AddStaff_KeyValidation.setText("")
        self.ui.AddStaff_CommentsValidation.setText("")
        self.ui.AddStaff_CodeValidation.setText("")
        
        self.ui.AddStaff_TitleValidation.setText(Validation.PresenceCheck(self.ui.AddStaff_TitleBox.text()))
        self.ui.AddStaff_KeyValidation.setText(Validation.PresenceCheck(self.ui.AddStaff_KeyWordsBox.text()))
        self.ui.AddStaff_CommentsValidation.setText(Validation.LengthCheckXL(self.ui.AddStaff_CommentsBox.text()))
        self.ui.AddStaff_CodeValidation.setText(Validation.CodeCheck(self.ui.AddStaff_CodeBox.text()))
        
        if self.ui.AddStaff_TitleValidation.text() == "" and self.ui.AddStaff_KeyValidation.text() == "" and self.ui.AddStaff_CommentsValidation.text() == "" and self.ui.AddStaff_CodeValidation.text() == "":
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("insert into Staff(Staff_ID,StaffName,Published,KeyWords,Comments)values(?,?,?,?,?)",self.ui.AddStaff_NumberBox.text(),self.ui.AddStaff_TitleBox.text(),self.ui.AddStaff_DateBox.text(),self.ui.AddStaff_KeyWordsBox.text(),self.ui.AddStaff_CommentsBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Employee Saved.')
            self.close()

    def BackButton(self):
        self.close()