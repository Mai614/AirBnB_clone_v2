#!/usr/bin/python3
"""
A Fabric script to clean outdated archives locally and remotely
"""
from fabric.api import *
from os.path import isdir, join

env.hosts = ['54.173.91.144', '54.157.134.6']

def do_local_clean(number=0):
    """
    Deletes out-of-date archives locally
    """
    number = int(number) + 1
    local_archives = sorted(run('ls -1t versions').split())
    for archive in local_archives[number:]:
        local('rm versions/{}'.format(archive))
    print("Local: Old archives deleted!")

def do_remote_clean(number=0):
    """
    Deletes out-of-date archives remotely
    """
    number = int(number) + 1
    with hide('running', 'output', 'commands'):
        remote_archives = sorted(run('ls -1t /data/web_static/releases').split())
    for archive in remote_archives[number:]:
        run('rm -rf /data/web_static/releases/{}'.format(archive))
    print("Remote: Old archives deleted!")

def do_clean(number=0):
    """
    Deletes out-of-date archives both locally and remotely
    """
    do_local_clean(number)
    do_remote_clean(number)

if __name__ == "__main__":
    do_clean()

