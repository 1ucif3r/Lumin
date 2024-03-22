# coding: utf-8
#!/usr/bin/env python
import os
import time
from time import sleep
from platform import system
import subprocess
from subprocess import check_call
from sys import argv
from genericpath import isfile
from traceback import print_tb
from pystyle import *
from colorama import Fore, init
from sys import stdout


cmd  = os.system("clear")

defaultpublickey  = "mypublickey.pem";


def intro():
    cmd  = os.system("clear")
    print("""
                                                                                          
                                                                                             
\033[94m                   ,▄▄▄       █▄▄▄,
\033[94m                ▄█████▄▄▄▄╓,   ██▓██▄
\033[94m            ▄▄██▓███▓███████████▓███▓█
\033[94m         ▄███▀█▓██████████████████████
\033[94m      ,███▀   █████████████████████▓██,      \033[0m\033[91m  
\033[94m     ███       ▀██████████████▓████▀╙▀██     \033[0m\033[91m 
\033[94m   ,██└            ██████████▓█¬      "██µ   \033[0m\033[91m ██╗     ██╗   ██╗███╗   ███╗██╗███╗   ██╗ \033[0m 
\033[94m  ╒██             ██████████▓█"         ██µ  \033[0m\033[91m ██║     ██║   ██║████╗ ████║██║████╗  ██║ \033[0m 
\033[94m  ██             ▄███████████▀           ██  \033[0m\033[91m ██║     ██║   ██║██╔████╔██║██║██╔██╗ ██║ \033[0m 
\033[94m ▐█▌            ▐█▓█████████▌            ▐█▌ \033[0m\033[91m ██║     ██║   ██║██║╚██╔╝██║██║██║╚██╗██║ \033[0m 
\033[94m ██            ,█▓██████████              ██ \033[0m\033[91m ███████╗╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║ \033[0m 
\033[94m ██            █▓████████▓█               ██ \033[0m\033[91m ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ \033[0m 
\033[94m ██⌐          ██████████▓█               ]██ \033[0m\033[1;31m       A Advance Steganography Tool       \033[0m 
\033[94m ▐██         ██████████▓█▀               ██▌ \033[0m\033[1;32m           Coded By © 1ucif3r             \033[0m 
\033[94m  ██▄       ▐███████████▌               ▐██  \033[0m\033[91m                                            \033[0m 
\033[94m   ██▄      █████████████▄      ,,,,   ▄██ █ \033[0m\033[91m                                            \033[0m     
\033[94m    ▀██      ████████████▓██████▓▓▓██████▄▄██▄
\033[94m     ╙██▄     ▀██▓██████████████████████▓▓▓█▓█⌐
\033[94m       ╙▀██▄    "▀███▓▓██▓▓▓███▀▀██████████████
\033[94m          ▀▀███▄g   `▀▀▀▀▀▀▀▄▄███▀▀,███████████
\033[94m              ▀▀▀███████████▀▀▀¬æ██████▓███████
\033[94m                                       ▀▀██████
\033[94m                                           ▀██
     
                           
                                                             
    \033[1;34m[1]-->Hide MSG in Image file          \033[1;34m[5]-->Extract MSG from IMG   
    \033[1;34m[2]-->Hide MSG in Video file          \033[1;34m[6]-->Extract MSG from VIDEO              
    \033[1;34m[3]-->Hide One file in Another file   \033[1;34m[7]-->Extract One file in Another file                        
    \033[1;34m[4]-->FileLock (SOON)                                                

    \033[1;34m[0]-->About Dev
    \033[1;34m[00]-->Exit

""") 
    stdout.write(Fore.LIGHTBLUE_EX+"╔═══"+Fore.LIGHTBLUE_EX+"["+Fore.RED+"root"+Fore.RED+ " @ " +Fore.RED+"Lumin"+Fore.LIGHTBLUE_EX+"]"+Fore.LIGHTBLUE_EX+"\n╚══"+Fore.RED+"# " +Fore.WHITE)
    choice = input()
    

    if choice  == "1" :
        print("\033[1;32m\nGenerating Both Public & Private Key ...")
        print("")
        os.system("python3 genkeys.py")
        print("")
        print("\033[1;32m================================================================")
        print("\033[1;31m[==]   Enter your Image path & secret Message Below  [==]   ")
        print("\033[1;32m================================================================")
        print("")
        imgpath = input("\033[1;31m>> \033[1;37mEnter Your image path : ")
        print("")
        secret  = input("\033[1;31m>> \033[1;37mEnter Your secret File : ")
        if not imgpath :
            print("\033[1;31m Pls Enter image path & secret")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
        else:
            print("")
            publickey = input("Enter your Public Key Manually or Leave it for the Default generated one :  ")
            print("")
            if not publickey:
                os.system("python3 img.py hide "+imgpath+" "+secret+" "+defaultpublickey+" output.png") 
            else :
                os.system("python3 img.py hide "+imgpath+" "+secret+" "+publickey+" output.png") 
        time.sleep(1)
        intro()
    
    elif choice  == "2" :
         print("")
         print("\033[1;32m================================================================")
         print("\033[1;31m[==]   Enter your Video path & secret Message Below  [==]   ")
         print("\033[1;32m================================================================")
         print("")
         vidpath = input("\033[1;31m>> \033[1;37mEnter Your Video path : ")
         print("")
         secret  = input("\033[1;31m>> \033[1;37mEnter Your secret File or Msg : ")
         print("")
         codecs  = input("\033[1;31m>> \033[1;37mChoice FFV1 or HFYU codecs  : ")
         if not vidpath :
            print("")
            print("\033[1;31m Pls Enter Video path & secret")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
         else:
            print("")
            publickey = input("Enter your Public Key Manually or Leave it for the Default generated one :  ")
            print("")
            if not publickey:
                os.system("python3 vid.py hide "+vidpath+" --output output.mkv --message "+secret+" --codec "+codecs+" --public_key "+defaultpublickey+"")  
            else :
                os.system("python3 vid.py hide "+vidpath+" --output output.mkv --message "+secret+" --codec "+codecs+" --public_key "+publickey+"")  
         time.sleep(1)
         intro()


    elif choice  == "3" :
         print("")
         print("\033[1;32m================================================================")
         print("\033[1;31m[==]   Enter your Both Files Below  [==]   ")
         print("\033[1;32m================================================================")
         print("")
         file1  = input("\033[1;31m>> \033[1;37mEnter Your 1st File path : ")
         print("")
         file2  = input("\033[1;31m>> \033[1;37mEnter Your 2st File path : ")
         print("")
         output  = input("\033[1;31m>> \033[1;37mEnter Your Output file name : ")
         if not file1 :
            print("")
            print("\033[1;31m Pls Enter 1st File Path")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
         elif not file2 :
            print("")
            print("\033[1;31m Pls Enter 2nd File Path")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
         elif not output :
            print("")
            print("\033[1;31m Pls Enter 2nd File Path")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
         else:
            print("")
            publickey = input("Enter your Public Key Manually or Leave it for the Default generated one :  ")
            print("")
            if not publickey:
                os.system("python3 file.py --hide --host "+file1+" --file "+file2+" --public-key "+defaultpublickey+" --output "+output+"")  
            else :
                os.system("python3 file.py --hide --host "+file1+" --file "+file2+" --public-key "+publickey+" --output "+output+"")  
         time.sleep(1)
         intro()
         
    elif choice  == "5" :
        print("")
        print("\033[1;32m================================================================")
        print("\033[1;31m[==]   Enter your Image path & Private Key Below  [==]   ")
        print("\033[1;32m================================================================")
        print("")
        imgpath = input("\033[1;31m>> \033[1;37mEnter Your image path : ")
        print("")
        privatekey  = input("\033[1;31m>> \033[1;37mEnter Your Private Key : ")
        print("")
        if not imgpath :
            print("")
            print("\033[1;31m Pls Enter image path & Private Key")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
        else:
            os.system("python3 img.py extract "+imgpath+" "+privatekey+" [extracted.txt]") 
        time.sleep(1)
        intro()

    elif choice  == "6" :
        print("")
        print("\033[1;32m================================================================")
        print("\033[1;31m[==]   Enter your Video path & Private Key Below  [==]   ")
        print("\033[1;32m================================================================")
        print("")
        videopath = input("\033[1;31m>> \033[1;37mEnter Your Video path : ")
        print("")
        privatekey  = input("\033[1;31m>> \033[1;37mEnter Your Private Key : ")
        print("")
        passphrase  = input("\033[1;31m>> \033[1;37mEnter Your Passphrase : ")
        print("")
        if not videopath :
            print("")
            print("\033[1;31m Pls Enter video path , Private Key & passphrase")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
        else:
            os.system("python3 vid.py unhide "+videopath+" --private_key "+privatekey+" --passphrase "+passphrase+"")  
        time.sleep(1)
        intro()

    elif choice  == "7" :
        print("")
        print("\033[1;32m================================================================")
        print("\033[1;31m[==]   Enter your Both Files Below  [==]   ")
        print("\033[1;32m================================================================")
        print("")
        file1  = input("\033[1;31m>> \033[1;37mEnter Your Hidden File path : ")
        print("")
        privatekey  = input("\033[1;31m>> \033[1;37mEnter Your Private Key : ")
        print("")
        passphrase  = input("\033[1;31m>> \033[1;37mEnter Your Passphrase : ")
        print("")
        outputfile  = input("\033[1;31m>> \033[1;37mEnter Your Output name : ")
        print("")
        if not file1 :
            print("")
            print("\033[1;31m Pls Enter video path , Private Key & passphrase")
            print("")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            print("")
            time.sleep(2)
        else:
            os.system("python file.py --unhide --host "+file1+" --private-key "+privatekey+" --output "+outputfile+" --passphrase "+passphrase+"")  
        time.sleep(1)
        intro()



    elif choice  == "0" :
        cmd = os.system("clear")
        print("""
              

          ]@                                                               ,$@'
          ]@@g                                                           ,@@@@
           %$$&Ng                                                     ,g@@$@@
           g@@@|*&$Nw,          ,g@@NM$$$gwwggg$$$$N@@gg,        ,g@N$W$|@$@g
            %@$M@ljg$$@$MNmgg@@M$l&@]N@@@@@@$$$$$@M$@@$@$@@gg@NM$@g$grl@M$&@`
            ,]@$@@L,*&MM|'"MW/$@@@@%@@@@@@@@@@@@@@@@R@$$$@}gM"'lMM$M,;@&$@Mg@`
            "$@$MM@,,jp@$%%"']Q@@@@@$@Mll$$$$@$$$%@$$@@@@P$""%%$$g@,,@MM$%@C
            w$&N@$@@gw;"$g|$,#U@@@@@l$$$$$$$$@@@@$@$@@@@@U@,ll$@*},y@@$$@$Lw
              *%@@$MMNN&R&$$L]W$@@M$$@$$$$$$$@@@@$@@$@@@@V@l$$@RN&NM$$$@@M`
                "&$@@gg,,$@&$L%,%@$$$P%$$$$@@@@$@P$@@@@@,@,$@B$,,lg@@@$"
                   *%@@$$|L]M&$]$@@@$@g@Ng$@$$@N@g@@$@@@[l&M@,l$$$@M'
                     *M%@@@@@@$@g@#@$$$%$ll$$$$$$$$$$$@Wl$@@@@@@MM*
                        $@@$$$@@@@@&@k"*N$$$$@@N*'g$$@@@@@@$$$@@\033[0m\033[91m                                           \033[0m 
                        '%@@@$@@@@@@@$@"        "$@@@@$@@$@@$$@F\033[0m\033[91m (                  (    (          (     \033[0m
                         ]@@@@j@@@@@@@@@Ng,,,,gg@@@@@@@@@$$$$@F \033[0m\033[91m )\ )          (    )\ ) )\ )       )\ )  \033[0m
                           %@@@l%@@l$$@@T%@M$T%@]$l$$@@@$@$$@F  \033[0m\033[91m(()/(    (     )\  (()/((()/(  (   (()/(  \033[0m
                           %@@@$$@@@@$@$$$@$@@@$@@$@@@$@$$@,,   \033[0m\033[91m /(_))   )\  (((_)  /(_))/(_)) )\   /(_)) \033[0m
                            $@@P*$@NN@@@@@@@@@@@@@@@NNNNNPP     \033[0m\033[91m(_))  _ ((_) )\___ (_)) (_))_|((_) (_))   \033[0m
                             @P $@F @ ,,,]L $  ,,,@ ,gggP       \033[0m\033[91m| |  | | | |((/ __||_ _|| |_  | __|| _ \  \033[0m
                                 @ww@,]@@@L,$,,,,]@gwgg         \033[0m\033[91m| |__| |_| | | (__  | | | __| | _| |   /  \033[0m
                                    $l'""]@T$lj@@@@l`'          \033[0m\033[91m|____|\___/   \___||___||_|   |___||_|_\  \033[0m    
                                       @@@@@@@@@@@
                                        "MN@@@BM
                                                
                                                              
\033[0m\033[92m          [!] Instagram : instagram.com/0x1ucif3r/     \033[0m
\033[0m\033[92m          [!] Website   : lucifer.sh/                        \033[0m
\033[0m\033[92m          [!] Github    : github.com/1ucif3r/                  \033[0m


""")
        time.sleep(5)
        intro()
        quit()
    elif choice  == "00":
        exit()

        
    
    
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()

intro()
    