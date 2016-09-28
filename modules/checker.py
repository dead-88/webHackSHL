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
import os
isnm=os.path.isfile("/usr/bin/nmap")
isfierce=os.path.isfile("/usr/bin/fierce")
ismap=os.path.isfile("/usr/bin/sqlmap")
isenum=os.path.isfile("/usr/bin/dnsenum")
isnikto=os.path.isfile("/usr/bin/nikto")
iswhatw=os.path.isfile("/usr/bin/whatweb")
iswp=os.path.isfile("/usr/bin/wpscan")

def installall():
    print """Para que este framework funcione correctamente, necesitas tener instaladas las siguientes herramientas:
    nmap, fierce, sqlmap, dnsenum, nikto, whatweb & wpscan. Al parecer hay herramientas faltantes en tu sistema!.
    ¿Deseas instalar todas las herramientas necesarias? Esto solo funciona con sistemas basados en Debian.
    """
    decision=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")
    if decision=="y":
        print "Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten."
        print "Añadiendo el repositorio temporal de Kali a tu lista de repossitorios ..."
        os.system("sudo echo -e '\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' | sudo tee -a /etc/apt/sources.list.d/kalitemp.list")
        print ""
        print "Actualizando tu lista de paquetes ..."
        os.system("sudo apt update")
        os.system("clear")
        print "Instalando los paquetes ..."
        os.system("sudo apt install nmap fierce sqlmap dnsenum nikto whatweb wpscan")
        print ""
        print "Removiendo el repositorio temporal de Kali Linux ..."
        os.system("sudo rm -rf /etc/apt/sources.list.d/kalitemp.list")
        os.system("clear")
        print "La instalacion se realizo correctamente."
        print "Todo lo necesario esta instalado, procediendo."
    elif decision == "n":
        print "Instalación abortada, saliendo ..."
        os._exit(0)
    else:
        print "Opcion incorrecta."
        installall()

def check():
    if isnm and isfierce and ismap and isenum and isnikto and iswhatw and iswp:
        print "Todo lo necesario esta instalado, procediendo."
    else:
        installall()
