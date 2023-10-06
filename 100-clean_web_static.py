#!/usr/bin/python3
"""
a Fabric script (based on the file 3-deploy_web_static.py)
"""

from fabric.api import *
from os.path import isdir, join
from datetime import datetime

env.hosts = ['54.173.91.144', '54.157.134.6']

def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 1:
        number = 1

    try:
        with hide('running', 'output', 'commands'):
            archives = sorted(run('ls -1t versions').split())

        for archive in archives[number:]:
            run('rm versions/{}'.format(archive))

        with hide('running', 'output', 'commands'):
            releases = sorted(run('ls -1t /data/web_static/releases').split())

        for release in releases[number:]:
            run('rm -rf /data/web_static/releases/{}'.format(release))

        print("Old archives and releases deleted!")
        return True
    except Exception as e:
        print(e)
        return False
