from caixa import CaixaCor
from PyQt6.QtWidgets import *
box = {}
n_box = 18
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        caixa1 = QListWidget()
        caixa2 = QLineEdit()

        tradutor ={0:'➗', 1:'✖️', 2:'➖', 3:'➕',
                   4:'7', 5:'8', 6:'9', 7:'❎', 
                   8:'4', 9:'5', 10:'6', 11:'CE',
                   12:'1', 13:'2', 14:'3', 15:'=',
                   16:',', 17:'0', 18:'.'}
        
        for i in range(n_box+1):
            box[i] = QPushButton(tradutor[i])
            box[i].setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
                               
        grid = QGridLayout()
        grid.addWidget(caixa1, 1, 1, 2, 4)
        grid.addWidget(caixa2, 3, 1, 1, 4)

        k = 0
        for i in range(4,9):
            for j in range(1,5):
                try:
                    if i == 7 and j == 4:
                        grid.addWidget(box[k], i, j, 2, 1)
                    elif i == 8 and j == 4:
                        pass
                    else:
                        grid.addWidget(box[k], i, j)
                    k+=1
                except:
                    pass
        
        self.setStyleSheet('''
            QPushButton{               
                font-size: 24px
            }   
            QLineEdit{
                font-size: 24px
            }           
            ''')

        componente = QWidget()
        componente.setLayout(grid)
        self.setCentralWidget(componente)


app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
