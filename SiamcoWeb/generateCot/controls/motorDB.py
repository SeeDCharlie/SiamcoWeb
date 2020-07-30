import psycopg2


class motor_pg():

    def __init__(self):
        self.initConection()
    
    def initConection(self):
        try :
            self.connection = psycopg2.connect(host="localhost", dbname="siamco_db", user="admseed", password="admseed777")
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

    def executeStatement(self, stmnt, dats = ()):
        self.cursor.execute(stmnt, dats)

    def getStatement(self, stmnt, dats = ()):
        self.executeStatement(stmnt, dats)
        return self.cursor
    
    def convertFetchOne(self, dats):
        l = dats[0][1:-1].replace('\"', "" )
        l = l.split(",")
        return l
    
    def existUser(self, userName, userPass):
        statement = 'select (fname, lname) from users where username = %s and userpass = %s'
        result = self.getStatement(statement, (userName, userPass)).fetchone()
        if result != None :
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



"""
m = motor_pg()

st = "select id_unid from measurement_units where code_dian = 'MTK'"
dats = ("admuno", "aduno")
stUno = 'select * from users '

m.getActivitiesForTable()

m.closeDB()
"""