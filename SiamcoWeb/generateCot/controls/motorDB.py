import psycopg2
from psycopg2 import sql


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

    def executeStatement(self, stmnt, dats=()):
        self.cursor.execute(stmnt, dats)

    def getStatement(self, stmnt, dats=()):
        self.executeStatement(stmnt, dats)
        return self.cursor

    def convertFetchOne(self, dats):
        l = dats[0][1:-1].replace('\"', "")
        l = l.split(",")
        return l

    def existUser(self, userName, userPass):
        statement = 'select (fname, lname) from users where username = %s and userpass = %s'
        result = self.getStatement(statement, (userName, userPass)).fetchone()
        if result != None:
            print("usuario correcto!")
            names = self.convertFetchOne(result)
            names[0] = names[0].split(" ")[0]
            names[1] = names[1].split(" ")[0]
            return names
        else:
            return False

    def getActivitiesForTable(self):
        st = """select a.cod, a.description, u.symbol, a.valueunit 
                from activities as a 
                inner join measurement_units as u 
                on a.unit  = u.id_unid"""

        return self.getStatement(st).fetchall()

    def saveQuotation(self, dicDats):
        try:
            self.cursor.execute("""
                            insert into cotizaciones(customerName,email,workplace,workAddress,
                            projectName,proNumber,durationWork,unitDuration,id_user,dateCreate,pdfTemplate,downloaded)
                            values(%(customerName)s,%(customerEmail)s,%(placeName)s,%(placeAddress)s,
                            %(projectName)s,%(proposalNumber)s,%(durationWork)s,%(unitDuration)s,
                            %(idAutor)s,%(dateToday)s,%(pdfTemplate)s,%(down)s);
                            """, dicDats)
            self.commit
            return True
        except Exception as error:
            print("error al subir el pedf a la db", error)
            return False

    def getIdUser(self, username):
        id_user = self.getStatement(
            "select id_user from users   where username = %s", (str(username),)
        ).fetchone()
        print("id_user encontrado : ", id_user[0])
        return id_user[0]

    def getTextPdf(self, idUser):
        try:
            text = self.getStatement("""
                        select pdftemplate from cotizaciones where id_user = %s and downloaded = False;
                        """, (str(idUser))).fetchone()
            print("")
            return text[0]
        except Exception as error:
            print("Error get text pdf : ", error)

    def updatePdfUser(self, id_user):
        try:
            self.executeStatement(
                "update cotizaciones set downloaded = %s", ('1'))
        except Exception as error:
            print("no se pudo actualizar la descarga. eror : ", error)

    def getImgEncabezado(self, idImg):
        return self.getStatement("select img from imagesDoc where id_img = %s", (idImg,))

    def getNewIdActi(self):
        idx = self.getStatement(
            'select cod from activities where cod =(select max(cod) from activities)').fetchall()[0][0]
        idx = 'S' + str(int(idx[1:])+1)
        return idx

    def deleteRegisters(self, idxs, tablename, nameid):
        try:
            for idx in idxs:
                self.executeStatement(sql.SQL("delete from {} where %s = %s")
                                      .format(sql.Identifier(tablename)), ( str(nameid), str(idx)))
                self.commit()
            return True
        except Exception as error:
            print("no se pudo eliminar de la tabla %s, error : %s" %
                  (tablename, str(error)))
            return False


"""m = motor_pg()

print("img : ", m.getNewIdActi() )

m.closeDB()"""
