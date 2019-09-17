from PyQt4 import uic,QtGui
import pyodbc

( Ui_Music_Podcasts_View, QDialog ) = uic.loadUiType( 'Music_Podcasts_View.ui' )

class Music_Podcasts_View ( QDialog ):
    """Music_Podcasts_View inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Music_Podcasts_View()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def RefreshPodcasts(self):
        link = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=E:\\paddy\Music System\MusicSystem.mdb;')
        point = link.cursor()
        point.execute("select * from Podcasts")
        records = point.fetchall()
        link.close()
        count = 0
        for record in records:
            self.ui.PodcastsView.removeRow(count)
            self.ui.PodcastsView.insertRow(count)
            self.ui.PodcastsView.setItem(count,0,QtGui.QTableWidgetItem(str(record[0])))
            self.ui.PodcastsView.setItem(count,1,QtGui.QTableWidgetItem(str(record[3])))
            self.ui.PodcastsView.setItem(count,2,QtGui.QTableWidgetItem(str(record[4])))
            count = count + 1

    def BackButton(self):
        self.close()