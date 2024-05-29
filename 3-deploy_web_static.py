#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.

    Fabric script (based on the file 1-pack_web_static.py) that distribute
    an archive to your web servers, using the function do_deploy

    Fabric script (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers, using the function deploy
"""
import os
from fabric.api import *
from datetime import datetime


@task
def do_pack():
    """
        Archieves the web_static directory
    """
    if not os.path.exists('versions'):
        local('mkdir -p versions')
    file_date = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = 'web_static_' + file_date + '.tgz'
    local("tar -cvzf versions/{} web_static".format(file_name))
    archived_path = "versions/{}".format(file_name)
    if os.path.exists(archived_path):
        return archived_path
    else:
        return None


env.user = 'ubuntu'
env.hosts = ['34.239.253.144', '3.84.255.96']
# env.key_filename = '~/.ssh/school'


@task
def do_deploy(archive_path):
    """
        deploys the codes on the two servers
    """
    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, '/tmp/', use_sudo=True).succeeded:
        return False
    file_path = archive_path.split('.')[0].split('/')[1]
    file_name = archive_path.split('/')[1]
    if run('mkdir -p /data/web_static/releases/{}/'.format(file_path)).failed:
        return False
    if run('tar -xzf /tmp/{}  -C /data/web_static/releases/{}/'.format
           (file_name, file_path)).failed:
        return False
    if run('sudo rm -rf /tmp/{}'.format(file_name)).failed:
        return False
    if run('sudo rm -rf /data/web_static/current').failed:
        return False
    src = "/data/web_static/releases/{}/web_static/*".format(file_path)
    des = "/data/web_static/releases/{}/".format(file_path)
    if run("sudo rsync -a {} {}".format(src, des)).failed:
        return False
    if run('sudo rm -rf /data/web_static/releases/{}/web_static'.format
           (file_path)).failed:
        return False
    if run("sudo ln -s {} /data/web_static/current".format(des)).failed:
        return False
    print("New version deployed!")
    return True


@task
def deploy():
    """
        creates and distributes an archive to your web servers
    """
    archived_path = do_pack()
    print(archived_path)
    if not archived_path:
        return False
    return do_deploy(archived_path)
