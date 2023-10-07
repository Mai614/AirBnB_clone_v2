#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if successful, None otherwise.
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        # Use capture to handle the output and errors properly
        result = local("tar -czvf versions/{} web_static".format(archive_name), capture=True)

        if result.succeeded:
            return "versions/{}".format(archive_name)
        else:
            return None
    except Exception as e:
        print("Error: {}".format(e))
        return None
