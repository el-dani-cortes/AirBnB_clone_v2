#!/usr/bin/python3
"""
Script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""
from fabric.api import run, local, put, cd, env
from datetime import datetime
import os
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    return do_deploy(archive_path)
