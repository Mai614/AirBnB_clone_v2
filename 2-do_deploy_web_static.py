#!/usr/bin/python3
"""
Fabric script for packing and deploying a web_static archive
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
        if not path.exists("versions"):
            local("mkdir -p versions")
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )
        local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error: {}".format(e))
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not path.exists(archive_path):
        print(f"Error: Archive not found at {archive_path}")
        return False

    try:
        compressed_file = path.basename(archive_path)
        file_name = compressed_file.split(".")[0]
        upload_path = f"/tmp/{compressed_file}"
        current_release = f'/data/web_static/releases/{file_name}'
        
        print(f"Uploading archive to {env.hosts}...")
        put(archive_path, upload_path)

        print(f"Removing existing release: {current_release}")
        run(f"rm -rf {current_release}")

        print(f"Creating new release directory: {current_release}")
        run(f"mkdir -p {current_release}")

        print(f"Extracting archive to {current_release}")
        run(f"tar -xzf {upload_path} -C {current_release}")

        print(f"Deleting uploaded archive: {upload_path}")
        run(f"rm -f {upload_path}")

        print("Updating symbolic link /data/web_static/current")
        run(f"rm -rf /data/web_static/current && ln -s {current_release} /data/web_static/current")

        print("Deployment completed successfully!")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
