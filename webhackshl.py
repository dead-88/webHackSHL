#!/usr/bin/python2
# encoding: utf-8
# Testing Web Framework - Copyright (C) <2016> - <Hanom1960>
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

import os
import argparse
from modules import adminder
#from modules import sqlitestmod
from modules import sqlimod
from modules import portsmod
from modules import fingerwebmod
from modules import checker
from modules import hashid

parser = argparse.ArgumentParser(prog='webhackshl.py',usage='python webhackshl.py',description='WebHackSHL es un conjunto de herramientas desarrollado por Security Hack Labs, para realizar auditorias de seguridad web desde basicas hasta avanzadas, diseñado especialmente para sistemas Debian o basados en el, como Kali Linux.')
parser.add_argument("-u", "--update", help="Actualiza WebHackSHL a la mas version mas reciente.", action="store_true")
args = parser.parse_args()

# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.update:   
       print "Actualizando el framework..."
       os.system("git pull")
       print "WebHackSHL actualizado correctamente."
       os._exit(0)


def gems():
    print "Revisando si Bundler esta instalado ..."
    gem=os.system("bundle | grep 'Bundle complete! 5 Gemfile dependencies, 15 gems now installed.'")
    if gem == 0:
        print "Bundler esta instalado. Continuando."
        pass
    else:
        print """Necesitas instalar Bundler, procediendo a la instalación.
Bundler es requerido por un escanner de vulnerabilidades, necesitas privilegios root o sudo para instalarlo.
Esto puede tomar un tiempo."""     
        inst = raw_input("Deseas continuar con la instalación? y/n : ")
        if inst=="y":
            print "Instalando bundler..."
            os.system("sudo gem install bundler && bundle install")
            pass
        elif inst=="n":
            print "Instalacion cancelada, esto traera problemas en la opcion d) del menú usando joomlavs. Continuando ..."
            pass

def logo():
    print """
 __    __     _                      _     __          __  
/ / /\ \ \___| |__   /\  /\__ _  ___| | __/ _\  /\  /\/ /  
\ \/  \/ / _ \ '_ \ / /_/ / _` |/ __| |/ /\ \  / /_/ / /   
 \  /\  /  __/ |_) / __  / (_| | (__|   < _\ \/ __  / /___ 
  \/  \/ \___|_.__/\/ /_/ \__,_|\___|_|\_\\\\__/\/ /_/\____/ 

    Programador: Eduard Eliecer Tolosa Toloza 
      XMPP/Email: tolosaeduard@cock.lu
    Security Hack Labs Team. @SecurityHackLab
    Blog: https://securityhacklabs.blogspot.com


Uso: python webhackshl.py -h - Muestra un mensaje de ayuda.
     python webhackshl.py -u - Actualiza WebHackSHL a la versión mas reciente.
"""

def disclaimer():
    print "Advertencia legal: El uso de WebHackSHL para atacar objetivos sin el consentimiento mutuo previo es ilegal. Es responsabilidad del usuario final a obedecer todas las leyes aplicables locales, estatales y federales. Los desarrolladores no asumen ninguna responsabilidad y no son responsables de cualquier mal uso o daño causado por este programa"
try:
    logo()
    print ""
    disclaimer()
    print ""
    gems()
    print ""
    checker.check()
    def webframework():
        print ""
        print """Selecciona una de las siguientes opciones.
        a) Buscar URLs vulnerables a SQLi, LFI, RCE, XSS.
        b) Realizar SQLi a una web vulnerable a SQLi
        c) Realizar un escaneo completo de un host, enumerar DNS, Bypassear Cloudflare y mas.
	d) Realizar pruebas de penetracion web y analisis de vulnerabilidades.
        e) Buscar el panel admin de un sitio web.
        f) Ataques a contraseñas y hashing.
        g) Salir.
        """
        sel=raw_input("Selecciona: ")
        if sel == "a":
            try:
                from modules import sqlitest
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "b":
            try:
                sqlimod.execute()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "c":
            try:
                portsmod.menu()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "d":
            try:
                fingerwebmod.execute()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "e":
            try:
                adminder.adminfind()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "f":
            try:
                hashid.menu()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "g":
            print "Saliendo."
                
        else:
            webframework()
    webframework()

except KeyboardInterrupt:
    print "Saliendo."
    pass
os._exit(0)
