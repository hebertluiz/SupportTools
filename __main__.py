import platform
from os import listdir,getenv
from time import sleep
from Support_shell import Shell



debug = True
ssh_bin = 'ssh '
openvpn_config_path = '/etc/openvpn/ccd/'

if platform.system() == 'Linux' and debug:
    openvpn_config_path='/home/hlsilva/scripts/Misc/ccd/'
    ssh_bin=''
    home= getenv("HOME") + "/"
elif platform.system() == 'Windows':
    openvpn_config_path='C:/Users/Hebert Silva/Scripts/Misc/ccd/'
    ssh_bin = 'putty -ssh '
    home = getenv("SystemDriv") + getenv("HOMEPATH") + "\\"
def get_hosts(directory):

    return listdir(directory);

def parseHostList(hostList):
    pass
    hostDict = {}

    for file in hostList:
        with open(openvpn_config_path + file) as f:
            lines=f.readlines()

            for l in lines:
                line = l.split()
                if  line[0] == 'ifconfig-push':
                    hostDict[file] = line[1]
    return hostList,hostDict

hosts,clientsDict = parseHostList(get_hosts(openvpn_config_path))


try:
    if __name__ == "__main__":
        shell = Shell(home, hosts, clientsDict, ssh_bin, debug)
        shell.cmdloop()
except KeyboardInterrupt:
       print("\nFinished by the user.")
       print("Exiting...")
       sleep(0.2)
       exit(0)