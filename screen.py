import sys
from walk import *

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from graph import *

class Widget(QWidget):


    def __init__(self,graph):
        super().__init__()

        self.button = QPushButton('RECREATE GRAPH', self)
        self.button.setStyleSheet("background-color: red")
        self.button.setToolTip("Press to refresh...")
        self.button.move(10, 10)
        self.button.clicked.connect(self.on_click)

        self.button2 = QPushButton('START TSP', self)
        self.button2.setStyleSheet("background-color: green")
        self.button2.setToolTip("Press to refresh...")
        self.button2.move(10, 130)
        self.button2.clicked.connect(self.startClick)

        self.msg = QMessageBox()
        self.msg.setWindowTitle("WARNING")
        self.e4 = QLineEdit(self)
        self.e4.setPlaceholderText("Num Of Nodes?..")
        self.e4.move(10,60)
        self.e4.setStyleSheet("background-color: yellow")
        self.e5 = QLineEdit(self)
        self.e5.setPlaceholderText("START NODE?..")
        self.e5.move(10, 90)
        self.e5.setStyleSheet("background-color: yellow")

        self.graph = graph

        self.label = QLabel(self)
        self.setStyleSheet("background-color: black;")

    def startClick(self):
        if len(self.e5.text()) == 0:
            self.msg.setText("YOU DIDNT SPECIFIED THE START NODE!")
            self.msg.exec_()
        if not self.e5.text() in self.graph.nodes:
            self.msg.setText("We couldnt find the that node!!! \nNode : "+self.e5.text())
            self.msg.exec_()
        else:
            start = self.e5.text()

            pathRenew(start,self.graph.adj,[],0,self.graph.edges_weights)
            shortpath(self.msg)
            self.button2.setText("START TSP")

            # print(str(walker.routes[0]))
    def on_click(self):

        if len(self.e4.text()) == 0 or int(self.e4.text())<3 or int(self.e4.text())>100 :
            self.e4.clear()
            self.e4.setPlaceholderText("min 4 max 99 !!!")
            self.msg.setText("node number is bound to min 4 max 99 !!!")
            self.msg.exec_()

        else:
            self.graph = Graph(int(self.e4.text()))
            self.update()


    def paintEvent(self, event):

        node_color={}
        colors = [Qt.blue,Qt.red,Qt.darkGray,Qt.darkGray,Qt.magenta,Qt.yellow,Qt.darkGreen,Qt.cyan]

        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        keys = list(self.graph.nodes1.keys())
        vals = list(self.graph.nodes1.values())

        #print("nodes == "+str(self.graph.nodes1))
        #for m in self.graph.nodes1:
         #   print(str(self.graph.nodes1[m][2]))

        for i in self.graph.nodes1:
            color = random.choice(colors)
            painter.setPen(QPen(color, 2, Qt.SolidLine))
            painter.setBrush(QBrush(color, Qt.SolidPattern))

            painter.drawEllipse(self.graph.nodes1[i][0],self.graph.nodes1[i][1], 10, 10, )

            painter.drawText(self.graph.nodes1[i][0]-10,self.graph.nodes1[i][1]-10,str(keys[vals.index(self.graph.nodes1[i])]))
            #print("ACTUAL name: "+str(i))

        for i, u in enumerate(self.graph.edges):
            color = random.choice(colors)
            painter.setPen(QPen(color, 2, Qt.SolidLine))
            painter.setBrush(QBrush(color, Qt.SolidPattern))
            #print("today  "+str(u[0])+ " tomorrow " + str(u[1]))

            painter.drawLine(self.graph.nodes1[u[0]][0],self.graph.nodes1[u[0]][1],self.graph.nodes1[u[1]][0],self.graph.nodes1[u[1]][1])

            painter.drawText((self.graph.nodes1[u[0]][0] + self.graph.nodes1[u[1]][0] )/2,((self.graph.nodes1[u[0]][1] +self.graph.nodes1[u[1]][1])/2),str(self.graph.edges_weights[i][2]))

            #print("DRAW FROM "+ u[0]+"to "+ u[1])

        #walk.dfs()