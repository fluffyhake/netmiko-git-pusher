
from netmiko import Netmiko
from getpass import getpass
import hosts

username = "haakonlab"
password = "lablab"

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
        "username" : "admin",
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
    },
}   
