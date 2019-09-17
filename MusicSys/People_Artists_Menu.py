from PyQt4 import uic
import People_Artists_View
import People_Artists_Add

( Ui_People_Artists_Menu, QDialog ) = uic.loadUiType( 'People_Artists_Menu.ui' )

class People_Artists_Menu ( QDialog ):
    """People_Artists_Menu inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Artists_Menu()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    
    def ViewArtistsButton(self):
        self.ArtistsViewForm = People_Artists_View.People_Artists_View()
        self.ArtistsViewForm.exec_()
    
    def AddArtistButton(self):
        self.ArtistAddForm = People_Artists_Add.People_Artists_Add()
        self.ArtistAddForm.exec_()
    
    def BackButton(self):
        self.close()
