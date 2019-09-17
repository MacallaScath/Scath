from PyQt4 import uic

( Ui_Validation, QDialog ) = uic.loadUiType( 'Validation.ui' )

class Validation ( QDialog ):
    """Validation inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Validation()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def PresenceCheck(input):
        if len(input) > 0:
            return ""
        else:
            return "Please enter some information."
    
    def LengthCheckXL(input):
        if len(input) < 51:
            return ""
        else:
            return "Please enter fewer characters."
    
    def LengthCheckL(input):
        if len(input) < 31:
            return ""
        else:
            return "Please enter fewer characters."
    
    def LengthCheck(input):
        if len(input) < 19:
            return ""
        else:
            return "Please enter fewer characters."
    
    def CodeCheck(input):
        if input == "cat":
            return ""
        else:
            return "Incorrect code."