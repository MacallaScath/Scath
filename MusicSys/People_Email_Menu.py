from PyQt4 import uic
import People_Email_Add
import People_Email_Send

( Ui_People_Email_Menu, QDialog ) = uic.loadUiType( 'People_Email_Menu.ui' )

class People_Email_Menu ( QDialog ):
    """People_Email_Menu inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Email_Menu()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def AddEmailButton(self):
        self.AddEmailForm = People_Email_Add.People_Email_Add()
        self.AddEmailForm.exec_()
    
    def SendEmailButton(self):
        self.SendEmailForm = People_Email_Send.People_Email_Send()
        self.SendEmailForm.exec_()

    def BackButton(self):
        self.close()