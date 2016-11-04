#!/usr/bin/python2
# encoding: utf-8
# Testing Web Framework - Copyright (C) <2016>
#
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

import sys
import subprocess
import os
import socket
import argparse
from modules import adminder
from modules import sqlimod
from modules import portsmod
from modules import fingerwebmod
from modules import checker
from modules import hashid
version='v1.5 Estable'

parser = argparse.ArgumentParser(prog='webhackshl.py',usage='python2 webhackshl.py',description='WebHackSHL es un conjunto de herramientas desarrollado por Security Hack Labs, para realizar auditorias de seguridad web desde basicas hasta avanzadas, diseñado especialmente para sistemas Debian o basados en el, como Kali Linux. Cualquier problema reportelo en Github o a nuestas cuentas de Email y/o Twitter.')
parser.add_argument("-u", "--update", help="Actualiza WebHackSHL a la mas version mas reciente.", action="store_true")
parser.add_argument("-ut", "--utools", help="Actualiza todas las herramientas Necesitadas por WebHackSHL en tu SO.", action="store_true")
parser.add_argument("-v", "--version", help="Version de WebHackSHL", action="store_true")
parser.add_argument("-nc", "--noconnection",help="Iniciar framework sin accesó a intermet.", action="store_true")
args = parser.parse_args()


# create launcher
def create_launcher():
    cwd = os.getcwd()
    filewrite = open("/usr/local/bin/webhackshl", "w")
    filewrite.write("#!/bin/sh\ncd %s\nchmod +x webhackshl\n./webhackshl $*" % (cwd))
    filewrite.close()
    subprocess.Popen("chmod +x /usr/local/bin/webhackshl", shell=True).wait()

# Chequear acceso a internet.
def check_internet():
    try:
        print("[*] Puedes iniciar con ./webhackshl --noconnection para saltar el paso de chequeo.")
        print("[*] Chequeando si tienes acceso a internet...")
        rhost = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        rhost.connect(('google.com', 0))
        rhost.settimeout(2)
        return 1

    except Exception:
        return 0

    except KeyboardInterrupt:
        print("\n")
        print("[*] Saliendo de WebHackSHL....")
        exit()
        sys.exit()

try:
    # Bypass network check with argument
    if not "--noconnection" in sys.argv[1:]:
        # check internet connection
        if check_internet() == 0:
            print ("[!] Unable to detect Internet connection. Needed for PTF.")
            print ("[!] We will now exit PTF. Launch again when you got a connection.")
            print ("[!] You can also run ptf with the --noconnection argument to bypass the network check.")
            sys.exit()

        # try to update ourself first
        print("[*] Actualizando webHackSHL... Antes de iniciar el framework.")
        subprocess.Popen("git pull", shell=True).wait()

    # create automatic launcher
    create_launcher()


except KeyboardInterrupt:
    print("\n")
    print("[*] Saliendo de WebHackSHL...")
    exit()
    sys.exit()

except Exception as e:
    print ("[!] Ah ocurrido un error.")
    print(("[!] Tienes un error en/con: " + str(e)))

# Aquí procesamos el accesó a el framework sin conexión a internet
if args.noconnection:
    print "Iniciando framework sin accesó a internet..."

# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.update:   
       print "Actualizando WebHackSHL..."
       os.system("git pull")
       print "WebHackSHL actualizado correctamente."
       os._exit(0)

# Aqui procesamos el update a la herramientas del sistema.
if args.utools:
    checker.cRojo("Iniciando la actualizacion de las Herramientas de tu sistema...")
    checker.checkali()
    os._exit(0)

# Version de la herramienta.
if args.version:
    print "Versión: ",version
    os._exit(0)

def logo():
    print """
 __    __     _                      _     __          __  
/ / /\ \ \___| |__   /\  /\__ _  ___| | __/ _\  /\  /\/ /
\ \/  \/ / _ \ '_ \ / /_/ / _` |/ __| |/ /\ \  / /_/ / /   
 \  /\  /  __/ |_) / __  / (_| | (__|   < _\ \/ __  / /___ 
  \/  \/ \___|_.__/\/ /_/ \__,_|\___|_|\_\\\\__/\/ /_/\____/ 

    Programador: Eduard Eliecer Tolosa Toloza
    Colaboradores: Deiber Mejia Lopez / Angel
      XMPP/Email: tolosaeduard@cock.lu
IRC: Server irc.stormbit.net | Canal #SHL | Puerto 6697 (SSL)
    Security Hack Labs Team. @SecurityHackLab
    Blog: https://securityhacklabs.blogspot.com


Uso: python2 webhackshl.py -h - Muestra un mensaje de ayuda.
     python2 webhackshl.py -u - Actualiza WebHackSHL a la versión mas reciente.
     python2 webhachshl.py -ut - Actualiza las Herramientas necesarias para WebHackSHL
"""

def disclaimer():
    checker.cRojo("Advertencia legal: El uso de WebHackSHL para atacar objetivos sin el consentimiento mutuo previo es ilegal. Es responsabilidad del usuario final a obedecer todas las leyes aplicables locales, estatales y federales. Los desarrolladores no asumen ninguna responsabilidad y no son responsables de cualquier mal uso o daño causado por este programa")
try:
    logo()
    print ""
    disclaimer()
    print ""
    checker.check()
    print ""
    checker.gems()
    print ""
    checker.dtor()
    def webframework():
        print ""
        checker.cAmarillo("""Selecciona una de las siguientes opciones.""")
        print """
	a) Buscar URLs vulnerables a SQLi, LFI, RCE, XSS.
        b) Realizar SQLi a una web vulnerable a SQLi.
        c) Realizar un escaneo completo de un host, enumerar DNS, Bypassear Cloudflare y mas.
	d) Realizar pruebas de penetracion web y analisis de vulnerabilidades.
        e) Buscar el panel admin de un sitio web.
        f) Ataques a contraseñas y hashing.
        g) Salir.
        """
        sel = raw_input("Selecciona: ")
        if sel == "a":
            try:
                os.system("python2 modules/sqlitest.py")    
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel.lower() == "b":
            try:
                sqlimod.execute()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel.lower() == "c":
            try:
                portsmod.menu()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel.lower() == "d":
            try:
                fingerwebmod.execute()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel.lower() == "e":
            try:
                adminder.adminfind()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel.lower() == "f":
            try:
                hashid.menu()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel.lower() == "g":
            print "[*] Saliendo de WeHackSHL..."
                
        else:
            checker.cRojo("""[!] Error de selección """)
            webframework()
    webframework()

except KeyboardInterrupt:
    print("\n")
    print("[*] Saliendo de WebHackSHL....")
    exit()
    sys.exit()
