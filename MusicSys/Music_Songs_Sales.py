from PyQt4 import uic,QtGui,QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyodbc
from Validation import Validation
import datetime
#import win32com.client as win32
#UNCOMMENT WHEN BACK ON WINDOWS

( Ui_Music_Songs_Sales, QDialog ) = uic.loadUiType( 'Music_Songs_Sales.ui' )

class Music_Songs_Sales ( QDialog ):
    """Music_Songs_Sales inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Songs_Sales()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def ViewSales(self):
        self.ui.SongSales_SongNumberBox.setText("")
        self.ui.SongSales_SongTitleBox.setText("")
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        if self.ui.SongSales_NumberSearch.text() != "" and self.ui.SongSales_TitleSearch.text() != "":
            point.execute('select * from Songs where Song_ID = ? and SongName = ?',self.ui.SongSales_NumberSearch.text(),self.ui.SongSales_TitleSearch.text())
        elif self.ui.SongSales_NumberSearch.text() != "":
            point.execute('select * from Songs where Song_ID = ?',self.ui.SongSales_NumberSearch.text())
        elif self.ui.SongSales_TitleSearch.text() != "":
            point.execute('select * from Songs where SongName = ?',self.ui.SongSales_TitleSearch.text())
        else:
            QtGui.QMessageBox.about(self,'Error','No Song Found.')
        song = point.fetchone()
        self.SearchRecord = song
        if len(song) > 0:
            self.ui.SongSales_SongNumberBox.setText(song[0])
            self.ui.SongSales_SongTitleBox.setText(song[1])
            self.ui.SongSales_SalesBoxJun15.setValue(song[5])
            self.ui.SongSales_SalesBoxJul15.setValue(song[6])
            self.ui.SongSales_SalesBoxAug15.setValue(song[7])
            self.ui.SongSales_SalesBoxSep15.setValue(song[8])
            self.ui.SongSales_SalesBoxOct15.setValue(song[9])
            self.ui.SongSales_SalesBoxNov15.setValue(song[10])
            self.ui.SongSales_SalesBoxDec15.setValue(song[11])
            self.ui.SongSales_SalesBoxJan16.setValue(song[12])
            self.ui.SongSales_SalesBoxFeb16.setValue(song[13])
            self.ui.SongSales_SalesBoxMar16.setValue(song[14])
            self.ui.SongSales_SalesBoxApr16.setValue(song[15])
            self.ui.SongSales_SalesBoxMay16.setValue(song[16])
                
        '''xl = win32.gencache.EnsureDispatch('Excel.Application')
        sheet = xl.Workbooks.Open('E:\\paddy\\Music System\\SongSales.xlsx')
        page = sheet.ActiveSheet
        xl.Visible = True
        count = 1
        while count < 50:
            page.Cells(count,1).Value = ""
            page.Cells(count,2).Value = ""
            count = count + 1
        page.Cells(1,1).Value = "June '15"
        page.Cells(2,1).Value = "July '15"
        page.Cells(3,1).Value = "August '15"
        page.Cells(4,1).Value = "September '15"
        page.Cells(5,1).Value = "October '15"
        page.Cells(6,1).Value = "November '15"
        page.Cells(7,1).Value = "December '15"
        page.Cells(8,1).Value = "January '16"
        page.Cells(9,1).Value = "February '16"
        page.Cells(10,1).Value = "March '16"
        page.Cells(11,1).Value = "April '16"
        page.Cells(12,1).Value = "May '16"
        page.Cells(1,2).Value = self.ui.SongSales_SalesBoxJun15.text()
        page.Cells(2,2).Value = self.ui.SongSales_SalesBoxJul15.text()
        page.Cells(3,2).Value = self.ui.SongSales_SalesBoxAug15.text()
        page.Cells(4,2).Value = self.ui.SongSales_SalesBoxSep15.text()
        page.Cells(5,2).Value = self.ui.SongSales_SalesBoxOct15.text()
        page.Cells(6,2).Value = self.ui.SongSales_SalesBoxNov15.text()
        page.Cells(7,2).Value = self.ui.SongSales_SalesBoxDec15.text()
        page.Cells(8,2).Value = self.ui.SongSales_SalesBoxJan16.text()
        page.Cells(9,2).Value = self.ui.SongSales_SalesBoxFeb16.text()
        page.Cells(10,2).Value = self.ui.SongSales_SalesBoxMar16.text()
        page.Cells(11,2).Value = self.ui.SongSales_SalesBoxApr16.text()
        page.Cells(12,2).Value = self.ui.SongSales_SalesBoxMay16.text()'''

    def Print(self):
        self.PrintPage = QPrinter()
        dialog = QPrintDialog(self.PrintPage,self)
        if not dialog.exec_():
            return
        HFormat = QTextBlockFormat()
        HFormat.setAlignment(Qt.AlignCenter)
        BFormat = QTextBlockFormat()
        BFormat.setAlignment(Qt.AlignJustify)
        HTFormat = QTextCharFormat()
        HTFormat.setFont(QFont("Times",20))
        BTFormat = QTextCharFormat()
        BTFormat.setFont(QFont("Times",15))
        
        Document = QTextDocument()
        Cursor = QTextCursor(Document)
        Cursor.insertBlock(HFormat)
        Cursor.insertText(self.ui.SongSales_SongNumberBox.text())
        Cursor.insertBlock(HFormat)
        Cursor.insertText(self.ui.SongSales_SongTitleBox.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertBlock(BFormat)
        Cursor.insertBlock(HFormat)
        Cursor.insertText("2015")
        Cursor.insertBlock(BFormat)
        Cursor.insertText("June: %s" %self.ui.SongSales_SalesBoxJun15.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("July: %s" %self.ui.SongSales_SalesBoxJul15.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("August: %s" %self.ui.SongSales_SalesBoxAug15.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("September: %s" %self.ui.SongSales_SalesBoxSep15.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("October: %s" %self.ui.SongSales_SalesBoxOct15.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("November: %s" %self.ui.SongSales_SalesBoxNov15.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("December: %s" %self.ui.SongSales_SalesBoxDec15.text())
        Cursor.insertBlock(HFormat)
        Cursor.insertText("2016")
        Cursor.insertBlock(BFormat)
        Cursor.insertText("January: %s" %self.ui.SongSales_SalesBoxJan16.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("February: %s" %self.ui.SongSales_SalesBoxFeb16.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("March: %s" %self.ui.SongSales_SalesBoxMar16.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("April: %s" %self.ui.SongSales_SalesBoxApr16.text())
        Cursor.insertBlock(BFormat)
        Cursor.insertText("May: %s" %self.ui.SongSales_SalesBoxMay16.text())
        Cursor.insertBlock(BFormat)
        
        MainFrame = Cursor.currentFrame()
        page = 1
        Document.print_(self.PrintPage)

    def SaveChanges(self):
        #add validation
        if self.ui.SongSales_SongTitleBox.text() != "":
            link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
            point = link.cursor()
            point.execute("update Songs set SalesJun15 = ? where Song_ID = ?",self.ui.SongSales_SalesBoxJun15.text(),self.ui.SongSales_SongNumberBox.text())
            link.commit()
            QtGui.QMessageBox.about(self,' ','Changes Saved.')
        
    def BackButton(self):
        self.close()