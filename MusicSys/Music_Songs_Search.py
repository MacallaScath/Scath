from PyQt4 import uic

( Ui_Music_Songs_Search, QDialog ) = uic.loadUiType( 'Music_Songs_Search.ui' )

class Music_Songs_Search ( QDialog ):
    """Music_Songs_Search inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Songs_Search()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    
    def SearchSongs(self):
        self.ui.SearchSongs_SongNumberBox.setText("")
        self.ui.SearchSongs_SongTitleBox.setText("")
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        if self.ui.SearchSongs_NumberSearch.text() != "" and self.ui.SearchSongs_TitleSearch.text() != "":
            point.execute('select * from Songs where Song_ID = ? and SongName = ?',self.ui.SearchSongs_NumberSearch.text(),self.ui.SearchSongs_TitleSearch.text())
        elif self.ui.SearchSongs_NumberSearch.text() != "":
            point.execute('select * from Songs where Song_ID = ?',self.ui.SearchSongs_NumberSearch.text())
        elif self.ui.SearchSongs_TitleSearch.text() != "":
            point.execute('select * from Songs where SongName = ?',self.ui.SearchSongs_TitleSearch.text())
        else:
            QtGui.QMessageBox.about(self,'Error','No Song Found.')
        song = point.fetchone()
        self.SearchRecord = song
        if len(song) > 0:
            self.ui.SearchSongs_SongNumberBox.setText(song[0])
            self.ui.SearchSongs_SongTitleBox.setText(song[1])
            self.ui.SearchSongs_SongDateBox.setDate(QtCore.QDate.fromString(song[2],'dd/MM/yyyy'))
            self.ui.SearchSongs_SongKeyBox.setText(song[3])
            self.ui.SearchSongs_SongCommentsBox.setText(song[4])
    
    def SaveChanges(self):
        self.ui.SearchSongs_SongTitleValidation.setText("")
        self.ui.SearchSongs_SongKeyValidation.setText("")
        self.ui.SearchSongs_SongCommentsValidation.setText("")
        #self.ui.SearchSongs_SongCodeValidation.setText("")
        
        self.ui.SearchSongs_SongTitleValidation.setText(Validation.PresenceCheck(self.ui.SearchSongs_SongTitleBox.text()))
        self.ui.SearchSongs_SongKeyValidation.setText(Validation.PresenceCheck(self.ui.SearchSongs_SongKeyBox.text()))
        self.ui.SearchSongs_SongCommentsValidation.setText(Validation.LengthCheckXL(self.ui.SearchSongs_SongCommentsBox.text()))
        #self.ui.SearchSongs_SongCodeValidation.setText(Validation.CodeCheck(self.ui.SearchSongs_SongCodeBox.text()))
        
        if self.ui.SearchSongs_SongTitleValidation.text() == "" and self.ui.SearchSongs_SongKeyValidation.text() == "" and self.ui.SearchSongs_SongCommentsValidation.text() == "":
            #and self.ui.SearchSongs_SongCodeValidation.text() == ""
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("update Songs set SongName = ?, Published = ?, KeyWords = ?, Comments = ? where Song_ID = ?",self.ui.SearchSongs_SongTitleBox.text(),self.ui.SearchSongs_SongDateBox.text(),self.ui.SearchSongs_SongKeyBox.text(),self.ui.SearchSongs_SongCommentsBox.text(),self.ui.SearchSongs_SongNumberBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Changes Saved.')

    def BackButton(self):
        self.close()