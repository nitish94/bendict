'''
Created on May 8, 2017

@author: nitish
'''
#-*-coding:utf8;-*-

import sys
from PyQt4 import QtCore, QtGui
import sqlite3 as sql

db = sql.connect('/opt/bendict/db/bendict.db')
cur=db.cursor()

def isEnglish(s):
    return len(s) == len(s.encode())

def transben(s):
    cur.execute("SELECT a.word FROM english a, bengali b where (a.w_id = b.w_id AND b.word LIKE '%s')"%s)
    lst = cur.fetchall()
    for i in lst:
        tv.insertHtml('<br>%s<br>'%i)
        
def transeng(s):
    cur.execute("SELECT b.word , b.oppo FROM english a, bengali b where (a.w_id = b.w_id AND a.word LIKE '%s')"%s)
    en,op = cur.fetchall()[0]
    tv.insertHtml('<b><u>TRANSLATE<u></b> <br> %s <br>'%en)
    tv.insertHtml('<br><br><u><b>OPPOSITE/বিপরীত</u></b><br>')
    op = eval(op)
    for i in op:
        tv.insertHtml('<br>%s<br>'%i)
    tv.insertHtml('<br><u><b>SIMILAR WORDS/ সমার্থক শব্দ</b></u>')
    transben(en)
        
    
    
        
def logcode():
    tv.insertHtml("<b><font color=red>NO SUCH WORD IN DICTIONARY</b></font>")

def printeng():
    word = entry.text()
    tv.clear()
    if isEnglish(word) == True:
        try:
            transeng(word)
        except IndexError:
            logcode()
        except TypeError:
            pass
    else:
        try:
            transben(word)
        except IndexError:
            logcode()



def b2_clicked():
    entry.clear()
#===============================================================================

app = QtGui.QApplication (sys.argv)
win = QtGui.QDialog()

grid = QtGui.QGridLayout()
win.setLayout(grid)

entry = QtGui.QLineEdit()
entry.resize(entry.sizeHint())
grid.addWidget(entry,0,0)

b1 = QtGui.QPushButton()
b1.setText("TRANSLATE")
b1.resize(b1.sizeHint())
grid.addWidget(b1,1,0, 1, 2)
b1.clicked.connect(printeng)

b2 = QtGui.QPushButton()
CIcon = QtGui.QPixmap("/opt/bendict/icons/clean.png")
b2.setIcon(QtGui.QIcon(CIcon))
b2.resize(b2.sizeHint())
grid.addWidget(b2,0,1, )
b2.clicked.connect(b2_clicked)

tv = QtGui.QTextEdit(win)
tv.setReadOnly(True)
tv.resize(tv.sizeHint())
grid.addWidget(tv,2,0, 1, 2)

# stting up icon

app_icon = QtGui.QIcon()
app_icon.addFile('/opt/bendict/icons/g16.png', QtCore.QSize(16,16))
app_icon.addFile('/opt/bendict/icons/g24.png', QtCore.QSize(24,24))
app_icon.addFile('/opt/bendict/icons/g32.png', QtCore.QSize(32,32))
app_icon.addFile('/opt/bendict/icons/g48.png', QtCore.QSize(48,48))
app_icon.addFile('/opt/bendict/icons/g256.png', QtCore.QSize(256,256))

app.setWindowIcon(app_icon)

win.setGeometry(100,100,280,300)
win.setWindowTitle("BEN DICT")
win.show()
sys.exit(app.exec_())

db.commit()
db.close()
