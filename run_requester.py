
from netmiko import Netmiko
from getpass import getpass

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

    except:
        print("Device does not support SSH :(")
        print("My lab is too old for this... i need to add telnet support")
        print("-" * 60)

