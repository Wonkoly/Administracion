# Librerias para la interfas grafica
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import  QDate 
from PyQt5 import QtCore

#Limbrerias de Sistema y Base de Datos
import sys 
import time
import datetime
import locale
import re

#Libreria de Funciones CRUD
from funcs import Crud

class Administracion(QMainWindow):
    
    def __init__(self):
        super().__init__()
       
        #----- Cargamos Hoja de Estilos
        #with open('python/Administracion/style.qss', 'r')  as style_file:
        #    style = style_file.read()
        #    self.setStyleSheet(style)
       
        #----- Cargamos la interfaz 
        self.init_ui()
        
        #----- Instancia de las Funciones Crud

        
    
    def init_ui(self):
       
        #----- VENTANA -----
        self.setFixedSize(440,635)
        self.setWindowTitle("Administración")
        self.setWindowIcon(QIcon("python/Administracion/rsc/qrscan.png")) 
        
        #------ Titulo de la ventana
        self.lbTitulo = QLabel("Administración de QRs",self)
        self.lbTitulo.setGeometry(100,10,300,30)
        self.lbTitulo.setFont(QFont("Cascadia Code", 14))
        self.lbTitulo.setAlignment(QtCore.Qt.AlignCenter)

        #----- ETIQUETAS y CAMPOS -----
        #----- ID
        self.lbID = QLabel("ID:",self)
        self.lbID.setGeometry(10,60,200,30)
        self.lbID.setFont(QFont("Cascadia Code", 14))
        self.lbID.setAlignment(QtCore.Qt.AlignRight)
    
        self.txtID = QLineEdit(self)
        self.txtID.setGeometry(230,60,200,30)
        self.txtID.setFont(QFont("Cascadia Code", 14))
        self.txtID.setAlignment(QtCore.Qt.AlignLeft)

        # Permitir unicamente enteros a 5 digitos
        self.txtID.setValidator(QIntValidator())
        self.txtID.setMaxLength(5)

        #----- Paterno
        self.lbPaterno = QLabel("Paterno:",self)
        self.lbPaterno.setGeometry(10,95,200,30)
        self.lbPaterno.setFont(QFont("Cascadia Code", 14))
        self.lbPaterno.setAlignment(QtCore.Qt.AlignRight) 
        
        self.txtPaterno = QLineEdit(self)
        self.txtPaterno.setGeometry(230,95,200,30)
        self.txtPaterno.setFont(QFont("Cascadia Code", 14))
        self.txtPaterno.setAlignment(QtCore.Qt.AlignLeft)

        #----- Materno
        self.lbMaterno = QLabel("Materno:",self)
        self.lbMaterno.setGeometry(10,130,200,30)
        self.lbMaterno.setFont(QFont("Cascadia Code", 14))
        self.lbMaterno.setAlignment(QtCore.Qt.AlignRight)

        self.txtMaterno = QLineEdit(self)
        self.txtMaterno.setGeometry(230,130,200,30)
        self.txtMaterno.setFont(QFont("Cascadia Code", 14))
        self.txtMaterno.setAlignment(QtCore.Qt.AlignLeft)

        #----- Nombre
        self.lbNombre = QLabel("Nombre:",self)
        self.lbNombre.setGeometry(10,165,200,30)
        self.lbNombre.setFont(QFont("Cascadia Code", 14))
        self.lbNombre.setAlignment(QtCore.Qt.AlignRight)
        
        self.txtNombre = QLineEdit(self)
        self.txtNombre.setGeometry(230,165,200,30)
        self.txtNombre.setFont(QFont("Cascadia Code", 14))
        self.txtNombre.setAlignment(QtCore.Qt.AlignLeft) 

        #----- CURP
        self.lbCurp = QLabel("CURP:",self)
        self.lbCurp.setGeometry(10,200,200,30)
        self.lbCurp.setFont(QFont("Cascadia Code", 14))
        self.lbCurp.setAlignment(QtCore.Qt.AlignRight) 

        self.txtCurp = QLineEdit(self)
        self.txtCurp.setGeometry(230,200,200,30)
        self.txtCurp.setFont(QFont("Cascadia Code", 14))
        self.txtCurp.setAlignment(QtCore.Qt.AlignLeft)
        self.txtCurp.setMaxLength(18)
        self.txtCurp.setPlaceholderText("EJMP10101MNEXXXA8") 

        #----- Fecha de Nacimiento
        self.lbFechaNacimiento = QLabel("Fecha Nacimiento:",self)
        self.lbFechaNacimiento.setGeometry(10,235,200,30)
        self.lbFechaNacimiento.setFont(QFont("Cascadia Code", 14))
        self.lbFechaNacimiento.setAlignment(QtCore.Qt.AlignRight)

        self.calendarioNacimiento = QDateEdit(self)
        self.calendarioNacimiento.setGeometry(230,235,200,30)
        self.calendarioNacimiento.setFont(QFont("Cascadia Code", 14))
        self.calendarioNacimiento.setAlignment(QtCore.Qt.AlignLeft)
        self.calendarioNacimiento.setCalendarPopup(True)

        #----- Correo
        self.lbCorreo = QLabel("Correo:",self)
        self.lbCorreo.setGeometry(10,270,200,30)
        self.lbCorreo.setFont(QFont("Cascadia Code", 14))
        self.lbCorreo.setAlignment(QtCore.Qt.AlignRight)

        self.txtCorreo = QLineEdit(self)
        self.txtCorreo.setGeometry(230,270,200,30)
        self.txtCorreo.setFont(QFont("Cascadia Code", 14))
        self.txtCorreo.setAlignment(QtCore.Qt.AlignLeft)
        
        #----- Fecha de Registro
        self.lbFechaRegistro = QLabel("Fecha Registro:",self)
        self.lbFechaRegistro.setGeometry(10,305,200,30)
        self.lbFechaRegistro.setFont(QFont("Cascadia Code", 14))
        self.lbFechaRegistro.setAlignment(QtCore.Qt.AlignRight)

        self.txtFechaRegistro = QLineEdit(self)
        self.txtFechaRegistro.setGeometry(230,305,200,30)
        self.txtFechaRegistro.setFont(QFont("Cascadia Code", 14))
        self.txtFechaRegistro.setAlignment(QtCore.Qt.AlignLeft)
        self.txtFechaRegistro.setEnabled(False)

        #----- ROL
        self.lbRol = QLabel("Rol:",self)
        self.lbRol.setGeometry(10,340,200,30)
        self.lbRol.setFont(QFont("Cascadia Code", 14))
        self.lbRol.setAlignment(QtCore.Qt.AlignRight)

        self.cbRol = QComboBox(self)
        self.cbRol.setGeometry(230,340,200,30)
        self.cbRol.setFont(QFont("Cascadia Code", 14)) 
        elementos = ["Administrativo","Estudiante","Externo","Operativo","Profesor"]
        self.cbRol.addItems(elementos)
        
        #----- QR
        self.lbQr = QLabel("QR:",self)
        self.lbQr.setGeometry(10,375,200,30)
        self.lbQr.setFont(QFont("Cascadia Code", 14))
        self.lbQr.setAlignment(QtCore.Qt.AlignRight) 
        
        self.txtQr = QLineEdit(self)
        self.txtQr.setGeometry(230,375,200,30)
        self.txtQr.setFont(QFont("Consolas",8))
        self.txtQr.setAlignment(QtCore.Qt.AlignLeft) 
        self.txtQr.setEnabled(False)
        
        #---- Imagen de QR
        self.lbGif = QLabel(self)
        self.lbGif.setGeometry(240,430,180,180)
        self.lbGif.setStyleSheet("background-color:#000000;")
        self.imgGif = QMovie(r"C:\Users\soporte\Desktop\Python BD\Administracion\qr1.gif")
        self.lbGif.setMovie(self.imgGif)
        self.lbGif.setScaledContents(True)
        self.imgGif.start()

        #----- BOTONES -----
        #---- Registrar 
        self.btnRegistrar = QPushButton(self)
        self.btnRegistrar.setGeometry(10,410,200,40)
        self.btnRegistrar.setText("Registrar")
        self.btnRegistrar.setFont(QFont("Cascadia Code", 14))   
        # self.btnRegistrar.clicked.connect()
        
        #---- Buscar
        self.btnBuscar = QPushButton(self)
        self.btnBuscar.setGeometry(10,455,200,40)
        self.btnBuscar.setText("Buscar")
        self.btnBuscar.setFont(QFont("Cascadia Code", 14))     

        #---- Actualizar
        self.btnActualizar = QPushButton(self)
        self.btnActualizar.setGeometry(10,500,200,40)
        self.btnActualizar.setText("Actualizar")
        self.btnActualizar.setFont(QFont("Cascadia Code", 14))
        
        #---- Eliminar
        self.btnEliminar = QPushButton(self)
        self.btnEliminar.setGeometry(10,545,200,40)
        self.btnEliminar.setText("Eliminar")
        self.btnEliminar.setFont(QFont("Cascadia Code", 14))  

        #---- Cancelar
        self.btnCancelar = QPushButton(self)
        self.btnCancelar.setGeometry(10,590,200,40)
        self.btnCancelar.setText("Cancelar")
        self.btnCancelar.setFont(QFont("Cascadia Code", 14))
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv) #Instancia para las funciones basicas de la interfaz grafica
    adminView = Administracion() #Instancia de la interfaz grafica a cargar
    adminView.show() #Mostramos la interfaz
    sys.exit(app.exec()) #Inicia bucle principal de la aplicacion