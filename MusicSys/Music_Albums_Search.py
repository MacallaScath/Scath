from PyQt4 import uic,QtGui,QtCore
import pyodbc
from Validation import Validation

( Ui_Music_Albums_Search, QDialog ) = uic.loadUiType( 'Music_Albums_Search.ui' )

class Music_Albums_Search ( QDialog ):
    """Music_Albums_Search inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Albums_Search()
        self.ui.setupUi( self )
        self.SearchRecord = []

    def __del__ ( self ):
        self.ui = None

    def SearchAlbums(self):
        self.ui.SearchAlbums_AlbumNumberBox.setText("")
        self.ui.SearchAlbums_AlbumTitleBox.setText("")
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        if self.ui.SearchAlbums_NumberSearch.text() != "" and self.ui.SearchAlbums_TitleSearch.text() != "":
            point.execute('select * from Albums where Album_ID = ? and AlbumName = ?',self.ui.SearchAlbums_NumberSearch.text(),self.ui.SearchAlbums_TitleSearch.text())
        elif self.ui.SearchAlbums_NumberSearch.text() != "":
            point.execute('select * from Albums where Album_ID = ?',self.ui.SearchAlbums_NumberSearch.text())
        elif self.ui.SearchAlbums_TitleSearch.text() != "":
            point.execute('select * from Albums where AlbumName = ?',self.ui.SearchAlbums_TitleSearch.text())
        else:
            QtGui.QMessageBox.about(self,'Error','No Album Found.')
        album = point.fetchone()
        self.SearchRecord = album
        if len(album) > 0:
            self.ui.SearchAlbums_AlbumNumberBox.setText(album[0])
            self.ui.SearchAlbums_AlbumTitleBox.setText(album[1])
            self.ui.SearchAlbums_AlbumDateBox.setDate(QtCore.QDate.fromString(album[2],'dd/MM/yyyy'))
            self.ui.SearchAlbums_AlbumKeyBox.setText(album[3])
            self.ui.SearchAlbums_AlbumCommentsBox.setText(album[4])
    
    def SaveChanges(self):
        self.ui.SearchAlbums_AlbumTitleValidation.setText("")
        self.ui.SearchAlbums_AlbumKeyValidation.setText("")
        self.ui.SearchAlbums_AlbumCommentsValidation.setText("")
        #self.ui.SearchAlbums_AlbumCodeValidation.setText("")
        
        self.ui.SearchAlbums_AlbumTitleValidation.setText(Validation.PresenceCheck(self.ui.SearchAlbums_AlbumTitleBox.text()))
        self.ui.SearchAlbums_AlbumKeyValidation.setText(Validation.PresenceCheck(self.ui.SearchAlbums_AlbumKeyBox.text()))
        self.ui.SearchAlbums_AlbumCommentsValidation.setText(Validation.LengthCheckXL(self.ui.SearchAlbums_AlbumCommentsBox.text()))
        #self.ui.SearchAlbums_AlbumCodeValidation.setText(Validation.CodeCheck(self.ui.SearchAlbums_AlbumCodeBox.text()))
        
        if self.ui.SearchAlbums_AlbumTitleValidation.text() == "" and self.ui.SearchAlbums_AlbumKeyValidation.text() == "" and self.ui.SearchAlbums_AlbumCommentsValidation.text() == "":
            #and self.ui.SearchAlbums_AlbumCodeValidation.text() == ""
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("update Albums set AlbumName = ?, Published = ?, KeyWords = ?, Comments = ? where Album_ID = ?",self.ui.SearchAlbums_AlbumTitleBox.text(),self.ui.SearchAlbums_AlbumDateBox.text(),self.ui.SearchAlbums_AlbumKeyBox.text(),self.ui.SearchAlbums_AlbumCommentsBox.text(),self.ui.SearchAlbums_AlbumNumberBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Changes Saved.')
    
    def BackButton(self):
        self.close()