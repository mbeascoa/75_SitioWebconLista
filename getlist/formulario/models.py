import cx_Oracle


class Cliente:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "javaoracle", "localhost/XE")

    def altaCliente(self,nombre,ape1,ape2,domi,ciud,sx,datosSO,com):
        cursor = self.connection.cursor()
        try:
            ConsultaAlta = ("INSERT INTO clientesAlumnos "
                                "VALUES (:P1, :P2, :P3, :P4, :P5, :P6, :P7,:P8)")

            datosAlta = (nombre,ape1,ape2,domi,ciud,sx,datosSO,com)

            cursor.execute(ConsultaAlta, datosAlta)
            numeroRegistros=cursor.rowcount
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)
            numeroRegistros=error
        return numeroRegistros