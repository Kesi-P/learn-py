import sys
import math

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button:
	def __init__(self,text,results):
		self.b = QPushButton(str(text))
		self.text = text
		self.results = results
		self.b.clicked.connect(lambda: self.handleInput(self.text))

	def handleInput(self,v):
		print(v)

		if v == '=':
			res = eval(self.results.text())
			self.results.setText(str(res))
		elif v == 'AC': #clear every input
			self.results.setText('')
		elif v == '√':
			value = float(self.results.text())
			new_value = str(math.sqrt(value))
			self.results.setText(new_value)
		elif v =='CE':
			current_value = self.results.text()
			inputs = [current_value[i:i + 1] for i in range(0, len(current_value), 1)]
			pop_last = inputs.pop()
			new_value = ''.join(map(str,inputs))
			self.results.setText(new_value)
			#easiest way
			#self.results.setText(current_value[:-1})

		else:
			current_value = self.results.text()
			new_value = current_value + str(v)
			self.results.setText(new_value)


class Appication(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Calculaor')
		self.CreateApp()

	def CreateApp(self):

		#Creat grid
		grid = QGridLayout()
		results = QLineEdit()

		buttons =['AC','CE','√','%',
		          7,8,9,'*',
		          4,5,6,'-',
		          1,2,3,'+',
		          0,'.','=']
		row =4
		col =0

		grid.addWidget(results,0,0,4,4)

		for button in buttons:
			if col > 3:
				col = 0
				row += 1

			buttonObject = Button(button,results)

			if button == 0:
				grid.addWidget(buttonObject.b, row, col, 1, 2)
				col += 1
			else:
				grid.addWidget(buttonObject.b,row,col,1,1)
			col += 1

		self.setLayout(grid)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Appication()
	sys.exit(app.exec_())

