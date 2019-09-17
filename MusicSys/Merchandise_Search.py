from PyQt4 import uic,QtGui,QtCore
import pyodbc
from Validation import Validation

( Ui_Merchandise_Search, QDialog ) = uic.loadUiType( 'Merchandise_Search.ui' )

class Merchandise_Search ( QDialog ):
    """Merchandise_Search inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Merchandise_Search()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def SearchMerchandise(self):
        self.ui.SearchMerchandise_MerchandiseNumberBox.setText("")
        self.ui.SearchMerchandise_MerchandiseTitleBox.setText("")
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        if self.ui.SearchMerchandise_NumberSearch.text() != "" and self.ui.SearchMerchandise_TitleSearch.text() != "":
            point.execute('select * from Merchandise where Merchandise_ID = ? and MerchandiseName = ?',self.ui.SearchMerchandise_NumberSearch.text(),self.ui.SearchMerchandise_TitleSearch.text())
        elif self.ui.SearchMerchandise_NumberSearch.text() != "":
            point.execute('select * from Merchandise where Merchandise_ID = ?',self.ui.SearchMerchandise_NumberSearch.text())
        elif self.ui.SearchMerchandise_TitleSearch.text() != "":
            point.execute('select * from Merchandise where MerchandiseName = ?',self.ui.SearchMerchandise_TitleSearch.text())
        else:
            QtGui.QMessageBox.about(self,'Error','No Item Found.')
        merch = point.fetchone()
        self.SearchRecord = merch
        if len(merch) > 0:
            self.ui.SearchMerchandise_MerchandiseNumberBox.setText(merch[0])
            self.ui.SearchMerchandise_MerchandiseTitleBox.setText(merch[1])
            self.ui.SearchMerchandise_MerchandiseDateBox.setDate(QtCore.QDate.fromString(merch[2],'dd/MM/yyyy'))
            self.ui.SearchMerchandise_MerchandiseKeyBox.setText(merch[3])
            self.ui.SearchMerchandise_MerchandiseCommentsBox.setText(merch[4])
    
    def SaveChanges(self):
        self.ui.SearchMerchandise_MerchandiseTitleValidation.setText("")
        self.ui.SearchMerchandise_MerchandiseKeyValidation.setText("")
        self.ui.SearchMerchandise_MerchandiseCommentsValidation.setText("")
        #self.ui.SearchMerchandise_MerchandiseCodeValidation.setText("")
        
        self.ui.SearchMerchandise_MerchandiseTitleValidation.setText(Validation.PresenceCheck(self.ui.SearchMerchandise_MerchandiseTitleBox.text()))
        self.ui.SearchMerchandise_MerchandiseKeyValidation.setText(Validation.PresenceCheck(self.ui.SearchMerchandise_MerchandiseKeyBox.text()))
        self.ui.SearchMerchandise_MerchandiseCommentsValidation.setText(Validation.LengthCheckXL(self.ui.SearchMerchandise_MerchandiseCommentsBox.text()))
        #self.ui.SearchMerchandise_MerchandiseCodeValidation.setText(Validation.CodeCheck(self.ui.SearchMerchandise_MerchandiseCodeBox.text()))
        
        if self.ui.SearchMerchandise_MerchandiseTitleValidation.text() == "" and self.ui.SearchMerchandise_MerchandiseKeyValidation.text() == "" and self.ui.SearchMerchandise_MerchandiseCommentsValidation.text() == "":
            #and self.ui.SearchMerchandise_MerchandiseCodeValidation.text() == ""
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("update Merchandise set MerchandiseName = ?, Published = ?, KeyWords = ?, Comments = ? where Merchandise_ID = ?",self.ui.SearchMerchandise_MerchandiseTitleBox.text(),self.ui.SearchMerchandise_MerchandiseDateBox.text(),self.ui.SearchMerchandise_MerchandiseKeyBox.text(),self.ui.SearchMerchandise_MerchandiseCommentsBox.text(),self.ui.SearchMerchandise_MerchandiseNumberBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Changes Saved.')
    
    def BackButton(self):
        self.close()