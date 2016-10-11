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
import portsmod
import checker

def whatw():
    web=portsmod.host()
    checker.cAmarillo("Obteniendo informacion del sitio web.")
    print ""
    subprocess.call(["whatweb","-v",web])
    execute()
def nickscan():
    web=portsmod.host()
    checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando nikto...")
    subprocess.call(["nikto","-no404","-host",web])
    execute()
def joomsc():
    web=portsmod.host()
    checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando joomlavs...")
    subprocess.call(["chmod","+x","joomlavs"])
    subprocess.call(["./joomlavs","-u",web,"-a"])
    execute()
def joomsctor():
    web=host=portsmod.host()
    checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando joomlavs usando TOR...")
    subprocess.call(["chmod","+x","joomlavs"])
    subprocess.call(["./joomlavs","-u",web,"--proxy","SOCKS5://127.0.0.1:9050","-a"])
    execute()

def wordpresscan():
    web=portsmod.host()
    checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando wpscan...")
    subprocess.call(["sudo","wpscan","-u",web,"--enumerate","p","--enumerate","t","--enumerate","u"])
    execute()
def wordpresscantor():
    web=portsmod.host()
    checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando wpscan...")
    subprocess.call(["sudo","wpscan","-u",web,"--enumerate","p","--enumerate","t","--enumerate","u","--proxy","socks5://127.0.0.1:9050"])
    execute()

def execute():
    checker.cAmarillo("Seleccina una de las siguientes opciones:")
    print """
    a) Obtener informacion del sistio web, servidor, Ip, CMS, Software del servidor y mas.
    b) Buscar vulnerabilidades web usando nikto.
    c) Buscar vulnerabilidades web de sitios web Joomla.
    d) Buscar vulnerabilidades web de sitios web Joomla usando TOR.
    e) Buscar vulnerabilidades web de sitios web con WordPress
    f) Buscar vulnerabilidades web de sitios web con WordPress usando TOR.
    g) Salir."""
    sel=raw_input("Introduce tu opcion: ")
    if sel== "a":
        whatw()
    elif sel == "b":
        nickscan()
    elif sel == "c":
        joomsc()
    elif sel == "d":
        joomsctor()
    elif sel == "e":
        wordpresscan()
    elif sel == "f":
        wordpresscantor()
    elif sel == "g":
        print "Saliendo."
    else:
        execute()
