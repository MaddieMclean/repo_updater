import subprocess
import argparse
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

command = {
    'clone': clone,
    'pull': pull
}


def git(cmd):
    return ['git'] + cmd.split()


def clone(repo):
    subprocess.call(git(f'clone https://github.com/steeleye/{repo}.git'))


def pull(repo):
    path = os.getcwd()
    subprocess.call(git(f'-C {path}/{repo} pull'))


def process(action):
    for repo in repos:
        try:
            action(repo)
        except NotADirectoryError as e:
            # in the case of pull
            print(f'{repo} not found')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-exc', '--exclude', required=False, type=str)
    parser.add_argument('-cmd', '--command', required=True, type=str)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    cmd = args.command()
    cmd = cmd.lower()
    process(command[cmd])


if __name__ == '__main__':
    main()
