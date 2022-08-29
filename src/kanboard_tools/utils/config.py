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

'''
ssh -L 127.0.0.1:10081:netops10.network.ops.bj1.wormpex.com:5432  jingyu.wang@netops2.network.ops.bj1.wormpex.com
'''
def main():
    global PARSER 
    
    args = PARSER.parse_args()
   
    _config_path = args.config
    if _config_path is None:
        _config_path = '/Users/jingyu.wang/soft/mysoft/dev/python/kanboard_tools/config/config.ini'
        assert os.path.exists(_config_path) is True, f"{_config_path} is not exit!"
        
    config = read_config(_config_path)


if __name__ == '__main__':
    main()
       

  