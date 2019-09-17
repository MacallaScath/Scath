from PyQt4 import uic
import smtplib
import pyodbc

( Ui_People_Email_Send, QDialog ) = uic.loadUiType( 'People_Email_Send.ui' )

class People_Email_Send ( QDialog ):
    """People_Email_Send inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_People_Email_Send()
        self.ui.setupUi( self )
        

    def __del__ ( self ):
        self.ui = None

    def RefreshAlbums(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Albums")
        albums = point.fetchall()
        #add details in reverse order
        self.ui.SendEmail_AlbumTitle1.setText()
        self.ui.SendEmail_AlbumNumber1.setText()
        self.ui.SendEmail_AlbumTitle2.setText()
        self.ui.SendEmail_AlbumNumber2.setText()
        self.ui.SendEmail_AlbumTitle3.setText()
        self.ui.SendEmail_AlbumNumber3.setText()

    def SendEmailButton(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Emails")
        emails = point.fetchall()
        link.close()
        for email in emails:
            HOST = "monstercat.server.com"
            SUBJECT = SendEmail_HeaderBox.text()
            TO = email[3]
            FROM = "newsletter@monster.cat"
            text = SendEmail_BodyBox.text()
            BODY = ("From: %s" % FROM,
                    "To: %s" % TO,
                    "Subject: %s" % SUBJECT ,
                    "",
                    self.ui.SendEmail_BodyBox.text()
                    )
            server = smtplib.SMTP(HOST)
            server.sendmail(FROM, [TO], BODY)
            server.quit()
        
    def BackButton(self):
        self.close()