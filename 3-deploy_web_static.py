#!/usr/bin/python3
"""
A Fabric script that creates and distributes an archive to web servers
"""

from fabric.api import env, local, put, run
from os import path
from datetime import datetime

env.hosts = ["54.173.91.144", "54.157.134.6"]

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        local("mkdir -p versions")
        date = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            date.year, date.month, date.day,
            date.hour, date.minute, date.second
        )
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error: {}".format(e))
        return None

def do_deploy(archive_path):
    """
    Distributes archives to web servers
    Args:
        archive_path: path to local archive to be uploaded
    """
    if not path.exists(archive_path):
        return False
    try:
        file_name = path.basename(archive_path).split(".")[0]
        upload_path = "/tmp/{}".format(path.basename(archive_path))
        current_release = '/data/web_static/releases/{}'.format(file_name)

        put(archive_path, upload_path)

        run("mkdir -p {}".format(current_release))
        run("tar -xzf {} -C {}".format(upload_path, current_release))
        run("rm -f {}".format(upload_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(current_release))

        return True
    except Exception as e:
        print("Error: {}".format(e))
        return False

def deploy():
    """
    Creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
