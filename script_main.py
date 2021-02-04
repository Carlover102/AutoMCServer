#The os library is for running Bash commands in Python
import os
#The time library is for pauses in between commands
import time
#The socket library is for getting web information. In this case it's used for getting your computer's ip address to help you connect to the server.
import socket

def install():
  os.system('wget -O VServer.jar "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"')
def remove():
  os.system('sudo rm VServer.jar')

#Gets your computer ip address to help with connecting to the server later.
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        
    except Exception:
        IP = '127.0.0.1'
        
    finally:
        s.close()
        
    return IP

#Assigns your ip to a variable for use later.
ip = get_ip()

#Formats files for the Minecraft Server and Starts it.
def EULA():
  #Runs the bash script to generate the eula.txt file.
  os.system("java Xmx-1024M Xms-1024M -jar VServer.jar nogui")
  
  #Clears the terminal screen.
  os.system("clear")
    
    #Opens the User License Agreement text file in write mode.
  rf = open("eula.txt","w+")
    
    #Re-writes the text inside of the User License Agreement file as to accept it.
  rf.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n")
  rf.write("#Tue Feb 02 17:36:11 EST 2021\n")
  rf.write("eula=true")
    
    #Closes and saves the file.
  rf.close()
    
    #Prints the ip address of your computer that was collected earlier as to let you connect to the Minecraft Server.
  print(f"Type '{ip}' into the server address bar when the server has started.")
  time.sleep(3)
  print("Starting Server...")
  time.sleep(2)
  os.system("clear")
    
    #Re-runs the bash script as to start the Minecraft Server.
  os.system("java Xmx-1024M Xms-1024M -jar VServer.jar nogui")
   

#Runs the eula acceptance code.
EULA()
