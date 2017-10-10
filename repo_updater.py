import subprocess
import os

repos = {
    'commons-sink',
    'commons-shredder',
    'commons-bootstrap',
    'commons-email',
    'commons-fix',
    'sink-router',
    'sink-import-handler',
    'sink-eml-handler',
    'sink-task-handler',
    'sink-bootstrap-handler',
    'sink-trayport-handler',
    'sink-raw-handler',
    'sink-cse-handler',
    'sink-dlq-router',
    'sink-csv2mail-handler',
    'sink-shredder-task'
}


def git(cmd):
    return ['git'] + cmd.split()


def clone(repo):
    subprocess.call(git(f'clone https://github.com/steeleye/{repo}.git'))


def pull(repo):
    path = os.getcwd()
    subprocess.call(git(f'-C {path}/{repo} pull'))


for repo in repos:
    try:
        # clone(repo)
        pull(repo)
    except NotADirectoryError as e:
        print(f'{repo} not found')
