import sys
import os
import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class AddressBar(QLineEdit):
	def __init__(self):
		super().__init__()

	def mousePressEvent(self,e):  #input
		self.selectAll()

class App(QFrame):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Web Browser')
		self.CreateApp()
		#self.setBaseSize(1366,768)
		self.setMinimumSize(1366,768)
		self.setWindowIcon(QIcon('logo.png'))

	def CreateApp(self):
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)

		#Create Tabs
		self.tabbar = QTabBar(movable = True, tabsClosable = True)
		self.tabbar.tabCloseRequested.connect(self.CloseTab)
		self.tabbar.tabBarClicked.connect(self.SwitchTag)

		self.tabbar.setCurrentIndex(0)
		self.tabbar.setDrawBase(False)
		#shortcut
		self.shortCutNewTab = QShortcut(QKeySequence('ctrl+T'),self)
		self.shortCutNewTab.activated.connect(self.AddTab)
		self.shortCatReload = QShortcut(QKeySequence('ctrl+R'),self)
		self.shortCatReload.activated.connect(self.Reload)

		#Keep track of tabs
		self.tabCount = 0
		self.tabs =[]

		#Create AddressBar
		self.Toolbar = QWidget()
		self.Toolbar.setObjectName('Toolbar')
		self.ToolbarLayout = QHBoxLayout()
		self.addressbar = AddressBar()

		#set main view
		self.container = QWidget()
		self.container.layout = QStackedLayout()
		self.container.setLayout(self.container.layout)



		#New tab button
		self.AddTabButton = QPushButton('+')
		self.addressbar.returnPressed.connect(self.BrowseTo)
		self.AddTabButton.clicked.connect(self.AddTab)


		#set Toolbar Buttons
		self.BackButton = QPushButton('<')
		self.BackButton.clicked.connect(self.GoBack)

		self.ForwardButton = QPushButton('>')
		self.ForwardButton.clicked.connect(self.GoForward)

		self.ReloadButton = QPushButton('R')
		self.ReloadButton.clicked.connect(self.Reload)

		#bulit
		self.Toolbar.setLayout(self.ToolbarLayout)
		self.ToolbarLayout.addWidget(self.BackButton)
		self.ToolbarLayout.addWidget(self.ForwardButton)
		self.ToolbarLayout.addWidget(self.addressbar)
		self.ToolbarLayout.addWidget(self.AddTabButton)
		self.ToolbarLayout.addWidget(self.ReloadButton)
		self.layout.addWidget(self.tabbar)
		self.layout.addWidget(self.Toolbar)
		self.layout.addWidget(self.container)

		self.setLayout(self.layout)
		self.AddTab()
		self.show()

	def CloseTab(self, i):
		self.tabbar.removeTab(i)

	def AddTab(self):
		i = self.tabCount

		self.tabs.append(QWidget())
		self.tabs[i].layout = QVBoxLayout()
		self.tabs[i].setObjectName('tab' + str(i))
		#open web view
		self.tabs[i].content = QWebEngineView()
		self.tabs[i].content.load(QUrl.fromUserInput('http://www.google.com'))

		self.tabs[i].content1 = QWebEngineView()
		self.tabs[i].content1.load(QUrl.fromUserInput('http://www.google.com'))

		self.tabs[i].content.titleChanged.connect(lambda :self.SetTabContent(i, 'title'))
		self.tabs[i].content.iconChanged.connect(lambda :self.SetTabContent(i, 'icon'))
		self.tabs[i].content.urlChanged.connect(lambda :self.SetTabContent(i,'url'))

		#add webview to tabs layout
		self.tabs[i].splitview = QSplitter()
		self.tabs[i].layout.addWidget(self.tabs[i].splitview)

		self.tabs[i].splitview.addWidget(self.tabs[i].content)

		#set top layout tab from [] to layout
		self.tabs[i].setLayout(self.tabs[i].layout)

		#Add tab to top level stackdwidget
		self.container.layout.addWidget(self.tabs[i])
		self.container.layout.setCurrentWidget(self.tabs[i])

		#set the tab at top of screen
		self.tabbar.addTab('New Tab')
		self.tabbar.setTabData(i,{'object':'tab'+str(i), 'initial':i})
		print('td: ',self.tabbar.tabData(i)['object'])

		self.tabbar.setCurrentIndex(i)

		self.tabCount += 1

	def SwitchTag(self ,i):
		if self.tabbar.tabData(i):
			tab_data = self.tabbar.tabData(i)['object']
			print('tab',tab_data)
			tab_content = self.findChild(QWidget, tab_data)
			self.container.layout.setCurrentWidget(tab_content)
			new_url = tab_content.content.url().toString()
			self.addressbar.setText(new_url)

	def BrowseTo(self):
		text = self.addressbar.text()
		print(text)
		i = self.tabbar.currentIndex()
		tab = self.tabbar.tabData(i)['object']
		wv = self.findChild(QWidget, tab).content

		if 'http' not in text:
			if '.' not in text:
				url = "https://www.google.com/search?q="+text
			else:
				url = 'http://'+ text
		else:
			url = text

		wv.load(QUrl.fromUserInput(url))

	def SetTabContent(self,i,type):
		# self.tabs[i].objectName = tab1
		# self.tabbar.tabData(i)['object'] = tab1
		tab_name = self.tabs[i].objectName()
		#tab1
		count =0
		running = True
		current_tab = self.tabbar.tabData(self.tabbar.currentIndex())['object']
		if current_tab == tab_name and type == 'url':
			new_url = self.findChild(QWidget, tab_name).content.url().toString()
			self.addressbar.setText(new_url)
			return False

		while running:
			tab_data_name = self.tabbar.tabData(count)
			if count >= 99:
				running = False
			if tab_name == tab_data_name['object']:
				if type == 'title':
					newTitle = self.findChild(QWidget,tab_name).content.title()
					self.tabbar.setTabText(count,newTitle)
				elif type == 'icon':
					newIcon = self.findChild(QWidget,tab_name).content.icon()
					self.tabbar.setTabIcon(count,newIcon)
				running = False
			else:
				count += 1

	def GoBack(self):
		activeIndex = self.tabbar.currentIndex()
		tab_name = self.tabbar.tabData(activeIndex)['object']
		tab_content = self.findChild(QWidget, tab_name).content

		tab_content.back()

	def GoForward(self):
		activeIndex = self.tabbar.currentIndex()
		tab_name = self.tabbar.tabData(activeIndex)['object']
		tab_content = self.findChild(QWidget, tab_name).content

		tab_content.forward()

	def Reload(self):
		activeIndex = self.tabbar.currentIndex()
		tab_name = self.tabbar.tabData(activeIndex)['object']
		tab_content = self.findChild(QWidget, tab_name).content

		tab_content.reload()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '667'

	window = App()

	with open('style.css','r') as style:
		app.setStyleSheet(style.read())

	sys.exit(app.exec_())
