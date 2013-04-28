#!/usr/bin/env python
#-*- coding:utf-8 -*-

from os import getenv, path, mkdir
from ConfigParser import ConfigParser
import base64


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
        
        return (username,base64.standard_b64decode(password))
        
    else:
        return None

if __name__ == "__main__":
    if exists_config_file():
        manager.read (config_file)

        password = manager.get ("login","password")
        manager.set('login', 'password', base64.standard_b64encode(password))
        with open(config_file, "w") as f:
            manager.write(f)

