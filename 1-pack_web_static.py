#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local, task
from datetime import datetime
from os import path


@task
def do_pack():
    """
        Archieves the web_static directory
    """
    if not path.exists('versions'):
        local('mkdir -p versions')
    file_date = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = 'web_static_' + file_date + '.tgz'
    local("tar -cvzf ./versions/{} web_static".format(file_name))
    file_path = "./versions/{}".format(file_name)
    if path.exists(file_path):
        return file_path
    else:
        return None
