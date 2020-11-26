import os
from netmiko import Netmiko
from getpass import getpass
from datetime import datetime
import time

currenttime = datetime.now()
currenttimerightformat = currenttime.strftime("%d/%m/%Y %H:%M:%S")

username = "haakonlab"
password = "lablab" #(or getpass)

my_devices = {
    "lab-dist-sw" : {
        "host" : "192.168.66.10",
        "username" : username,
        "secret" : password,
        "password" : password,
        "device_type" : "cisco_ios"
    },

        "lab-l3-switch-1" : {
        "host" : "192.168.66.20",
        "username" : username,
        "secret" : password,
        "password" : password,
        "device_type" : "cisco_ios"
    },

        "lab-l3-switch-2" : {
        "host" : "192.168.66.21",
        "username" : username,
        "secret" : password,
        "password" : password,
        "device_type" : "cisco_ios"
    },

        "lab-l3-switch-3" : {
        "host" : "192.168.66.22",
        "username" : username,
        "secret" : password,
        "password" : password,
        "device_type" : "cisco_ios"
    },

        "lab-l3-switch-4" : {
        "host" : "192.168.66.23",
        "username" : username,
        "secret" : password,
        "password" : password,
        "device_type" : "cisco_ios"
    }
}   
#resets the running-config-all.txt file
configtxt = open("running-config-all.txt", "w")
configtxt.write("-" * 30 + currenttimerightformat + "-" * 30 + "\n" * 10)







for host in my_devices:
    print(host + ":")
    print(my_devices[host])
    print("-" *30 + "DEBUG" + "-" *30 )



for host in my_devices:
    print(host + ":")
    try:
        net_conn = Netmiko(**my_devices[host])
        net_conn.enable()
        output = net_conn.send_command("show run")
        print(output)
        print("-" * 60)
        try:
            print("Attempting to write to running-config-all.txt")
            configtxt.write("\n" *2 + "-" *30 + host + ":" +"-" *30)
            configtxt.write("\n" + output + "\n \n \n")

        except:
            print("Writing" + host + "to file went wrong...")

    except:
        print("Device does not support SSH :(")
        print("My lab is too old for this... i need to add telnet support")
        print("-" * 60)

configtxt.write("-" * 30 + "END" + "-" *30)


time.sleep(5)

#Removing secrets and sensitive info section:
censor_words = ["secret", "password", "username", "ip domain-name"]



with open('running-config-all.txt') as oldfile, open('running-config-all-censored.txt', 'w') as newfile:
    for line in oldfile:
        if not any(censor_word in line for censor_word in censor_words):
            newfile.write(line)

newfile.close()



