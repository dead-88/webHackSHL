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
import sys
import checker
import johnmod

def menu():
    checker.cAmarillo("\nElige la tarea que quieres realizar:")
    print """
    a) Identificacion de hashes.
    b) Desencriptación de hashes usando Hashcat + Wordlists.
    c) Desencriptacion de Hashes online y Wordlist para bruteforce.
    d) Retroceder.
    """
    option = raw_input("Introduce tu opcion: ")
    try:
        if option.lower() == "a":
            os.system("python2 modules/hashidentifier")
            menu()

        elif option.lower() == "b":
            os.system("python modules/password-recovery/hashcat")
            menu()
        elif option.lower() == "c":
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
        elif option.lower() == "d":
            print ""
            checker.cRojo("""[<] Retroceder...""")
        else:
            checker.cRojo("""[!] Error de selección """)
            menu()
    except KeyboardInterrupt:
        print("\n")
        print("[*] Saliendo de WebHackSHL....")
        exit()
        sys.exit()
