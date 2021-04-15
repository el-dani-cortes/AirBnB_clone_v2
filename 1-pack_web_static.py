#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import run, local, settings, hide
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo
    """
    # Create folder versions if not exists
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # current date and time
    now = datetime.now()
    t = now.strftime("%Y%m%d%H%M%S")

    # Build tgz filename
    file_name = "versions/web_static_" + t + ".tgz"

    # Create the compressed file with fab method
    try:
        local('tar -cvzf {} web_static'.format(file_name))
        return os.path.abspath(file_name)
    except:
        return None
