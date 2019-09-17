from PyQt4 import uic, QtGui #imports interface aspects of PyQT
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap #imports image manipulation aspects of QtGui
import datetime #imports module used for dealing with times and dates
import Music_Menu #imports another page so it can be opened
import People_Menu #imports another page so it can be opened
import Merchandise_Menu #imports another page so it can be opened

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' ) #links the code to a specific page

class MainWindow ( QMainWindow ): #sets the class of the current window
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ): #this code runs when the page initialises
        QMainWindow.__init__( self, parent ) #opens a window for the page to run in
        self.ui = Ui_MainWindow() #sets self.ui variable as current window
        self.ui.setupUi( self ) #sets up page
        self.ui.Main_Date.setText(str(datetime.date.today().strftime("%d/%m/%Y"))) #sets date on page to current date
        self.ui.Main_Logo.setPixmap(QtGui.QPixmap("E:\\paddy\logo.png")) #sets label on page to Monstercat logo

    def __del__ ( self ): #this code runs when the page is closed
        self.ui = None #the page closes

    def MusicMenuButton(self): #this code runs when the Music Menu button is pressed
        self.MusicMenuForm = Music_Menu.Music_Menu() #sets up a form which will load the next page
        self.MusicMenuForm.exec_() #loads the next page
    
    def PeopleMenuButton(self): #this code runs when the People Menu button is pressed
        self.PeopleMenuForm = People_Menu.People_Menu() #sets up a form which will load the next page
        self.PeopleMenuForm.exec_() #loads the next page
    
    def MerchandiseMenuButton(self): #this code runs when the Merchandise Menu button is pressed
        self.MerchandiseMenuForm = Merchandise_Menu.Merchandise_Menu() #sets up a form which will load the next page
        self.MerchandiseMenuForm.exec_() #loads the next page
    
    
