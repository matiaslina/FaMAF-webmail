#!/usr/bin/env python
#-*- coding:utf-8 -*-

from os import getenv, path, mkdir
from ConfigParser import ConfigParser


config_dir = getenv("HOME") + "/.famaf-webmail/"
config_file = config_dir + "config"

manager = ConfigParser()

def exists_config_file ():    
    return path.isdir(config_dir) and path.isfile(config_file)
    
def create_simple_config_file(username, password):
    if username == '' or password == '':
        return
    try:
        mkdir(config_dir, 0750)
    except OSError, e:
        print "Cannot make the directory %s. Directory already exists" % config_dir
    
    with open(config_file, 'w') as cfg:
        manager.add_section ('login')
        manager.set('login', 'username', username)
        manager.set('login', 'password', password)
        manager.write(cfg)
        
        print "Config file created!"
        
def get_user_data ():
    if exists_config_file():
        manager.read (config_file)
        
        username = manager.get("login", "username")
        password = manager.get("login", "password")
        
        return (username,password)
        
    else:
        return None
