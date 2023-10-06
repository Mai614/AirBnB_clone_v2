#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
"""
from fabric.api import *
from os.path import exists

env.hosts = ['54.173.91.144', '54.157.134.6']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        filename = archive_path.split('/')[-1]
        folder_name = filename.replace('.tgz', '')

        # Uncompress the archive to /data/web_static/releases/<folder_name>
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, folder_name))

        run('rm /tmp/{}'.format(filename))

        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))

        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
