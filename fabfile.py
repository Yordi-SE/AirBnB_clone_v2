#!/usr/bin/python3 
from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['100.24.242.101']

def run_remote_command():
    result = run('./0-setup_web_static.sh')
