#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jingyu Wang <badpasta@gmail.com>
#
# Environment:
# Python by version 3.9.

import configparser
import argparse
import os


PARSER = argparse.ArgumentParser()
PARSER.add_argument("--config", "-c", help="config file with path")

CONFIG = str()
DBCONFIG = dict()


def read_config(file_path):
    cf = configparser.ConfigParser()
    cf.read(file_path, encoding='utf-8')
    
    return cf

def check_db_config(config):
    if 'host' in config and \
        'passwd' in config and \
        'database' in config and \
        'port' in config and \
        'user' in config:
            
            return True
    
    return False


def isPath(config_path):
    if config_path is None:
        config_path = '/Users/jingyu.wang/soft/mysoft/dev/python/kanboard_tools/config/config_dev.ini'
        
    assert os.path.exists(config_path) is True, f"{config_path} is not exist!"
    
    return config_path


def initConfig():
    global PARSER, DBCONFIG
    
    args = PARSER.parse_args()
   
    _config_path = isPath(args.config)
    
    _config = read_config(_config_path)
   
    assert r'db_Kanboard' in  _config.sections(), "section db_Kanboard is not exist!"
    
    DBCONFIG = _config._sections['db_Kanboard']
        


'''
ssh -L 127.0.0.1:10081:netops10.network.ops.bj1.wormpex.com:5432  jingyu.wang@netops2.network.ops.bj1.wormpex.com
'''


if __name__ == '__main__':
    initConfig()
    print(type(DBCONFIG))
       

  