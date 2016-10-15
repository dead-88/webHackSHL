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
import checker

def host():
    global target
    target=raw_input("Introduce el host al que deseas hacerle el scan: ")
    if target == "":
        checker.cRojo("Host invalido.")
        host()
    else:
        return target
def port():
    global portnumber
    portnumber=raw_input("Introduce el puerto o los puertos que deseas escanear (Si deseas un rango de puertos, escribelos de la manera 1-1000): ")
    if portnumber == "":
        checker.cRojo("Puerto invalido.")
        port()
    else:
        return portnumber
def intensescan():
    host()
    checker.cRojo("Para este tipo de escaneo necesitas privilegios sudo o root, por favor introduzca su contrasena si no eres root.")
    subprocess.call(["sudo","nmap","-A","-T4","-sS","-Pn","-O","-sV","-p","1-10000","-v",target])
def fastscan():
    host()
    subprocess.call(["nmap","--open","-F",target])
def detectserv():
    host()
    subprocess.call(["nmap","-sP",target])
def detectver():
    host()
    subprocess.call(["nmap","-sV",target])
def escanport():
    host()
    port()
    subprocess.call(["nmap","-p",portnumber,target])
def recsystem():
    host()
    checker.cRojo("Para este tipo de escaneo necesitas privilegios sudo o root, por favor introduzca su contrasena si no eres root.")
    subprocess.call(["sudo","nmap","-O",target])
def enumdns():
    host()
    checker.cAmarillo("Enumerando DNS's")
    subprocess.call(["dnsenum",target])
def bypasscloud():
    host()
    checker.cAmarillo("Intentando Bypassear Cloudflare usando fierce...")
    subprocess.call(["fierce","-dns",target])
def menu():
    checker.cAmarillo("Por favor selecciona una de las siguientes opciones")
    print """
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
        menu()
    elif sel == "b":
        fastscan()
        menu()
    elif sel == "c":
        detectserv()
        menu()
    elif sel == "d":
        detectver()
        menu()
    elif sel == "e":
        escanport()
        menu()
    elif sel == "f":
        recsystem()
        menu()
    elif sel == "g":
        enumdns()
        menu()
    elif sel == "h":
        bypasscloud()
        menu()
    elif sel == "i":
        print "Saliendo."
    else:
        checker.cRojo("Opcion invalida.")
        menu()         
