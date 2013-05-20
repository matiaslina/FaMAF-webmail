#!/usr/bin/env python
#-*- coding:utf-8 -*-

# For make this with python3 and make it work, I need to drop out the base64 encode.
# This will be solved in the nexts days/weeks/years ;-)

from os import getenv, path, mkdir
from configparser import ConfigParser
#import base64


config_dir = getenv("HOME") + "/.famaf-webmail/"
config_file = config_dir + "config"

manager = ConfigParser()

def exists_config_file ():    
    return path.isdir(config_dir) and path.isfile(config_file)
    
def get_user_data ():
    if exists_config_file():
        manager.read (config_file)
        
        username = manager.get("login", "username")
        password = manager.get("login", "password")
        return (username,password)
        
    else:
        return None
        
def get_download_dir ():
    if exists_config_file():
        manager.read (config_file)
        
        return manager.get("Download", "dir")
    
    return None

if __name__ == "__main__":
    pass
#    if exists_config_file():
#        manager.read (config_file)
#
#        password = manager.get ("login","password")
#        manager.set('login', 'password', str(base64.standard_b64encode(bytes(password,'utf-8'))))
#        with open(config_file, "w") as f:
#            manager.write(f)

