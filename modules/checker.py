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
isrb=os.path.isfile("/usr/bin/ruby")
isnm=os.path.isfile("/usr/bin/nmap")
isfierce=os.path.isfile("/usr/bin/fierce") or os.path.isfile("/usr/bin/fierce.pl")
ismap=os.path.isfile("/usr/bin/sqlmap")
isenum=os.path.isfile("/usr/bin/dnsenum")
isnikto=os.path.isfile("/usr/bin/nikto")
iswhatw=os.path.isfile("/usr/bin/whatweb")
iswp=os.path.isfile("/usr/bin/wpscan")
iscurl=os.path.isfile("/usr/bin/curl")
isgit=os.path.isfile("/usr/bin/git")
def cRojo(prt): print("\033[91m {}\033[00m" .format(prt))
def cVerde(prt): print("\033[92m {}\033[00m" .format(prt))
def cAmarillo(prt): print("\033[93m {}\033[00m" .format(prt))
def cMoradoclaro(prt): print("\033[94m {}\033[00m" .format(prt))
def cMorado(prt): print("\033[95m {}\033[00m" .format(prt))
def cCian(prt): print("\033[96m {}\033[00m" .format(prt))
def cGrisclaro(prt): print("\033[97m {}\033[00m" .format(prt))
def cNegro(prt): print("\033[98m {}\033[00m" .format(prt))


def updatetools():
    cRojo("Desea actualizar las Herramientas utilizadas en tu Sistema?.")
    respuesta=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")
    if respuesta=="y":
        cAmarillo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        cAmarillo("Añadiendo el repositorio temporal de Kali a tu lista de repossitorios ...")
        os.system("sudo echo -e '\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' | sudo tee -a /etc/apt/sources.list.d/kalitemp.list")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo apt update")
        cAmarillo("actualizando Herramientas del sistema...")
        os.system("sudo apt install --only-upgrade nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby git curl")
        print ""
        cAmarillo("Removiendo el repositorio temporal de Kali Linux ...")
        os.system("sudo rm -rf /etc/apt/sources.list.d/kalitemp.list")
        cRojo("La actualizacion se realizo correctamente.")
        cRojo("Todo lo necesario esta actualizado, procediendo.")
    elif respuesta == "n":
        cAmarillo("Actualizacion abortada, saliendo ...")
        os._exit(0)
    else:
        cRojo("Opcion incorrecta.")
        updatetools()

def installall():
    cRojo("""Para que este framework funcione correctamente, necesitas tener instaladas las siguientes herramientas:
    nmap, fierce, sqlmap, dnsenum, nikto, whatweb & wpscan. Al parecer hay herramientas faltantes en tu sistema!.
    ¿Deseas instalar todas las herramientas necesarias? Esto solo funciona con sistemas basados en Debian.
    """)
    decision=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")
    if decision=="y":
        cRojo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        cAmarillo("Añadiendo el repositorio temporal de Kali a tu lista de repossitorios ...")
        os.system("sudo echo -e '\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' | sudo tee -a /etc/apt/sources.list.d/kalitemp.list")
        print ""
        cAmarillo("Importando las claves de GNU/Kali Linux para ejecutar la instalacion...")
        os.system("sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com ED444FF07D8D0BF6")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo apt update")
        os.system("clear")
        cAmarillo("Instalando los paquetes ...")
        os.system("sudo apt install nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby git curl")
        print ""
        cAmarillo("Removiendo el repositorio temporal de Kali Linux ...")
        os.system("sudo rm -rf /etc/apt/sources.list.d/kalitemp.list")
        os.system("clear")
        cVerde("La instalacion se realizo correctamente.")
        cVerde("Todo lo necesario esta instalado, procediendo.")
    elif decision == "n":
        print "Instalación abortada, saliendo ..."
        os._exit(0)
    else:
        print "Opcion incorrecta."
        installall()

def check():
    if isnm and isfierce and ismap and isenum and isnikto and iswhatw and iswp and isrb and isgit and iscurl:
        cVerde("Todo lo necesario esta instalado, procediendo.")
    else:
        installall()

def gems():
    cVerde("check Bundle...")
    gem=os.system("bundle | grep -q 'Bundle complete! 5 Gemfile dependencies, 15 gems now installed.'")
    if gem == 0:
        cVerde("Bundler - 0K")
        pass
    else:
        def gemsinstall():
            print """Necesitas instalar Bundler, procediendo a la instalación.
    Bundler es requerido por un escanner de vulnerabilidades, necesitas privilegios root o sudo para instalarlo.
    Esto puede tomar un tiempo."""     
            inst = raw_input("Deseas continuar con la instalación? y/n : ")
            if inst=="y":
                cAmarillo("Instalando bundler...")
                os.system("sudo gem install bundler && bundle install")
                pass
            elif inst=="n":
                cRojo("Instalacion cancelada, esto traera problemas en la opcion d) del menú usando joomlavs. Continuando...")
                pass
            else:
                print "Opción incorrecta.\n"
                gemsinstall()
        gemsinstall()


            
