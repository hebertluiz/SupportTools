from os import listdir
import json

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
    return hostDict

openvpn_config_path='C:/Users/Hebert Silva/Scripts/Misc/ccd/'
file_path = "C:\\Users\\Hebert Silva\\PycharmProjects\\SuportTools\\hosts.json"
servers = parseHostList(listdir(openvpn_config_path))

json_file = {"item":"server_list", "servers":[{'name':key, 'address':value} for key,value in servers.items()]}


try:
    with open(file_path, 'w+') as out_file:
        json.dump(json_file, out_file, indent=4, ensure_ascii=True)
except FileNotFoundError:
    raise

print (json.dumps(json_file, indent=4))


"""
d = {"name":"interpolator",
     "children":[{'name':key,"size":value} for key,value in sample.items()]}"""



