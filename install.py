import os

print("Downloading ... \n")
os.system("apt install python2 -y")
os.system("apt install pip2 -y")

os.system("pip2 install sys")
os.system("pip2 install threading")
os.system("pip2 install random")
os.system("pip2 install re")

os.system("git clone https://github.com/L-N-X-0/ddos_cyber")
os.system("cd ddos_cyber && python3 start.py")

