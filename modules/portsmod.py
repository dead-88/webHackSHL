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
def host():
    global host
    host=raw_input("Introduce el host al que deseas hacerle el scan: ")
    if host == "":
        print "Host invalido."
        menu()
    else:
        return host
def port():
    global port
    port=raw_input("Introduce el puerto o los puertos que deseas escanear (Si deseas un rango de puertos, escribelos de la manera 1-1000): ")
    if port == "":
        print "Puerto invalido."
        menu()
    else:
        return port
def intensescan():
    host()
    print "Para este tipo de escaneo necesitas privilegios sudo o root, por favor introduzca su contrasena si no eres root."
    subprocess.call(["sudo","nmap","-A","-T4","-sS","-Pn","-O","-sV","-p","1-10000","-v",host])
    menu()
def fastscan():
    host()
    subprocess.call(["nmap","-F",host])
    menu()
def detectserv():
    host()
    subprocess.call(["nmap","-sP",host])
    menu()
def detectver():
    host()
    subprocess.call(["nmap","-sV",host])
    menu()
def escanport():
    host()
    port()
    subprocess.call(["nmap","-p",port,host])
    menu()
def recsystem():
    host()
    print "Para este tipo de escaneo necesitas privilegios sudo o root, por favor introduzca su contrasena si no eres root."
    subprocess.call(["sudo","nmap","-O",host])
    menu()
def enumdns():
    host()
    print "Enumerando DNS's"
    subprocess.call(["dnsenum",host])
    menu()
def bypasscloud():
    host()
    print "Intentando Bypassear Cloudflare usando fierce..."
    subprocess.call(["fierce","-dns",host])
    menu()
def menu():
    print """Por favor selecciona una de las siguientes opciones
    a) Escaneo full de un host (Lento pero el mas completo).
    b) Escaneo rapido de un host.
    c) Detectar servidores corriendo de un host.
    d) Detectar versiones de los servicios corriendo en un host.
    e) Escanear un puerto especifico o un rango de puertos.
    f) Detectar el sistema operativo de un host.
    g) Enumerar los DNS de un host.
    h) Bypassear cloudflare.
    i) Salir.
    """
    sel=raw_input("Introduce tu opcion: ")
    if sel == "a":
        intensescan()
    elif sel == "b":
        fastscan()
    elif sel == "c":
        detectserv()
    elif sel == "d":
        detectver()
    elif sel == "e":
        escanport()
    elif sel == "f":
        recsystem()
    elif sel == "g":
        enumdns()
    elif sel == "h":
        bypasscloud()
    elif sel == "i":
        print "Saliendo."
    else:
        print "Opcion invalida."
        menu()         
