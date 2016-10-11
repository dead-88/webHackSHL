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
import checker

def menu():
    checker.cAmarillo("Elige la tarea que quieres realizar:")
    print """
    a) Identificacion de hashes.
    b) Desencriptacion de Hashes online y Wordlist para bruteforce.
    c) Salir.
    """
    option=raw_input("Introduce tu opcion: ")
    try:
        if option == "a":
            os.system("python2 modules/hashidentifier")
            menu()
        elif option == "b":
            checker.cAmarillo("Utiliza las siguientes direcciones Web para buscar tus hash.")
            print """
            1) Para hash MD5 - https://hashkiller.co.uk/md5-decrypter.aspx
            2) Para hash Sha-1 - https://hashkiller.co.uk/sha1-decrypter.aspx
            3) Para claves WPA/WPA2 - https://hashkiller.co.uk/wpa-crack.aspx
            4) Para hash NTML https://hashkiller.co.uk/ntlm-decrypter.aspx
            """
            checker.cRojo("Adicionalmente puedes descargar tus wordlist para ataques de fuerza bruta directamente desde aquí: ")
            os.system("cat modules/wordlist/worlists.txt | curl -F 'sprunge=<-' http://sprunge.us")
            print ""
            
            menu()
        elif option == "c":
            print "Saliendo."
        else:
            menu()
    except KeyboardInterrupt:
        pass
