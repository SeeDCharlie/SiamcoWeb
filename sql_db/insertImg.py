import psycopg2


class motor_pg():

    def __init__(self):
        self.initConection()

    def initConection(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost", dbname="siamco_db", user="admseed", password="admseed777")
        except Exception as e:
            print("No fue pocible la coneccion a la base de datos, error : ", e)
        else:
            print("Conexion exitosa!!")
            self.cursor = self.connection.cursor()

    def closeDB(self):
        self.cursor.close()
        self.connection.close()
        print("base de datos cerrada!")

    def commit(self):
        self.connection.commit()
        
mot = motor_pg()

imgUno = open('codeImgUno.txt','r',encoding="utf8").read()
imgDos = open('codeImgDos.txt','r',encoding="utf8").read()

mot.cursor.execute("insert into imagesDoc(id_img, namimg, img) values(1,'encabezadoUno', %s)",(imgUno,))
#mot.cursor.execute("insert into imagesDoc(id_img, namimg, img) values(2,'encabezadoDos', %s)",(imgDos,))
mot.commit()
mot.closeDB()

print(imgUno)

