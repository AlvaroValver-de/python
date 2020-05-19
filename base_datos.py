import sqlite3

def conection():
    conexion = sqlite3.connect("base_de_datos")
    return conexion


def crear_tabla(conexion,nombre):
    micursor= conexion.cursor()
    cadena = "CREATE TABLE "+nombre+"(id INTEGER PRIMARY KEY,nombre VARCHAR(20) UNIQUE,x INTEGER , y INTEGER)"
    micursor.execute(cadena)
    conexion.commit()
    conexion.close()


    
def ingresa(conexion,nombre,x,y,tabla):
    cadena ="INSERT INTO "+tabla+" VALUES(NULL,"+"'"+nombre+"',"+str(x)+","+str(y)+")"
    cursor = conexion.cursor()
    cursor.execute(cadena)
    conexion.commit()
    conexion.close()

def ingresa_arreglo(conexion,arreglo,tabla):
    cursor = conexion.cursor()
    cadena = "INSERT INTO "+tabla+" VALUES(NULL,?,?,?)"
    cursor.executemany(cadena,arreglo)
    conexion.commit()
    conexion.close()


def eliminar_tabla(conexion,nombre):
    cursor = conexion.cursor()
    cadena="DROP TABLE "+nombre
    cursor.execute(cadena)
    conexion.commit()
    conexion.close()


def eliminar_registro(conexion,nombre,tabla):
    cursor = conexion.cursor()
    cadena = "DELETE FROM "+tabla+" WHERE nombre ='"+nombre+"'"
    cursor.execute(cadena)
    conexion.commit()
    conexion.close()
    reiniciar_id(conection(),tabla)

def ordenar_por(conexion,por,tabla):
    aux = "aux"
    crear_tabla(conection(),aux)
    cursor = conexion.cursor()
    cadena = "INSERT INTO "+aux+"(nombre,x,y) SELECT nombre,x,y FROM "+tabla+" ORDER BY "+por+" ASC"
    cursor.execute(cadena)
    conexion.commit()
    conexion.close()
    eliminar_tabla(conection(),tabla)
    renombrar_tabla(conection(),aux,tabla)


def mostrar(conexion,tabla):
    cursor = conexion.cursor()
    cadena = "SELECT*FROM "+tabla
    cursor.execute(cadena)
    aux = cursor.fetchall()
    conexion.close()
    for i in aux:
    
        print (i)


def reiniciar_id(conexion,tabla):
    aux = "aux"
    crear_tabla(conexion,aux)
    copiar_tabla(conection(),tabla,aux)
    eliminar_tabla(conection(),tabla)
    renombrar_tabla(conection(),aux,tabla)

def copiar_tabla(conexion,tabla,tabla1):
    cursor = conexion.cursor()
    cadena = "INSERT INTO "+tabla1+"(nombre,x,y) SELECT nombre,x,y FROM "+tabla
    cursor.execute(cadena)
    conexion.commit()
    conexion.close()


def renombrar_tabla(conexion,tabla,nuevo):
    cursor = conexion.cursor()
    cadena = "ALTER TABLE "+tabla+" RENAME TO "+nuevo
    cursor.execute(cadena)
    conexion.commit()
    conexion.close()


def promedio(conexion,tabla,columna):
    cursor = conexion.cursor()
    cursor.execute("SELECT AVG("+columna+") FROM "+tabla)
    promedio = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return promedio[0]


def longitud(conexion,tabla):
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM "+tabla)
    leng = cursor.fetchone()
    conexion.close()
    return leng[0]


def percentil(conexion,tabla,percen):
    cursor = conexion.cursor()
    longi = longitud(conection(),tabla)
    aux = longi*percen/100
    if aux%int(aux) != 0:
        aux = int(aux)+1
    cursor.execute("SELECT*FROM tabla WHERE id ="+str(aux))
    registro = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return registro
        
def regresar_datos(cursor,tabla,Id,columna):
    cursor.execute("SELECT "+columna+" FROM "+tabla+" WHERE id="+str(Id))
    aux = cursor.fetchone()
    return aux[0]


def varianza(conexion,tabla,columna):
    prome = promedio(conection(),tabla,columna)
    longi = longitud(conection(),tabla)
    cursor = conexion.cursor()
    cont = 0
    for i in range(1,longi+1):
        cont = cont + (regresar_datos(cursor,tabla,i,columna)-prome)**2
    conexion.close()
    return cont/(longi-1)


def desviacion_estandar(conexion,tabla,columna):
    return (varianza(conexion,tabla,columna))**(1/2)

tabla1 = "tabla1"
tabla ="tabla"
aux = "aux"
por = "x"
#eliminar_tabla(conection(),aux)
#crear_tabla(conection(),aux)
#ingresa(conection(),"juana",345.0000056,0.987654,tabla)
#copiar_tabla(conection(),tabla,tabla1)
regresar_datos(conection().cursor(),tabla,23,"nombre")
array1 = [("11",0.1,2),
        ("12",0.2,3),
        ("13",3213,3),
        ("14",0.0004,4),
        ("15",5312,5),
        ("16",632,6), 
        ("perro1",34320.324,53411.2645),
        ("vaca1",110.2456,302.87),
        ("musica1",32.056,223.256),
        ("pila1",22335.678,908.7656),
        ("community1",60000.78,406.78),
        ("solas1",6032.18,46.78),
        ("domenicana1",52311.67,721003.127),
        ("fly1",0.37,12.4123456),
        ("azul1",0.2267,12130.912089)
        ]

#ingresa_arreglo (conection(),array1,tabla)
#eliminar_registro(conection(),"1",tabla)
#ordenar_por(conection(),por,tabla)
#mostrar(conection(),tabla)
#print(promedio(conection(),tabla,por))
#print(percentil(conection(),tabla,50))
#print(varianza(conection(),tabla,por))
#print(desviacion_estandar(conection(),tabla,por))

