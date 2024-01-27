import pymysql

class Conexion:

    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__conexion = None
        self.__cursor = None
    
    def conectar(self):
        try:
            # Se crea la conexion
            self.__conexion = pymysql.connect(host=self.__host,
                                              user=self.__user, 
                                              password=self.__password,
                                              db=self.__database)
            # Se crea el cursor
            self.__cursor = self.__conexion.cursor()
            return True

        except Exception as e:
            return e

    def cerrar(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__conexion:
            self.__conexion.close()
            return "Conexion cerrada"
    
    def ejecutar_consulta(self, consulta):
        try:
            self.__cursor.execute(consulta)
            return self.__cursor.fetchall()
        except Exception as e: 
            return e
     
    def ejecutar_consulta_one(self, consulta):
        try:
            self.__cursor.execute(consulta)
            return self.__cursor.fetchone()
        except Exception as e: 
            return e
        
    def commit(self):
        self.__conexion.commit()