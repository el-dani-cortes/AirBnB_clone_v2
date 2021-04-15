#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from fabric.api import run, local, put, cd, env
from datetime import datetime
import os


env.hosts = ['ubuntu@35.196.3.110', 'ubuntu@34.74.150.12']
# env.hosts = ['57ad0975975c@f706bb2c.hbtn-cod.io']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    # Validate if the archive path does not exist
    if not os.path.exists(archive_path):
        return False
    try:
        # Get the file_name
        split_name = archive_path.split('/')
        file_name = split_name[1]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        file_path = file_name.split('.')
        file_path = '/data/web_static/releases/' + file_path[0]
        run("mkdir -p {}".format(file_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, file_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Move files to the rigth folder
        file_path_move = file_path + '/web_static'
        run("mv {}/* {}".format(file_path_move, file_path))

        # Remove path web_static
        run("rm -rf {}".format(file_path_move))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on
        # the web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s {} /data/web_static/current".format(file_path))
        return True
    except:
        return False
