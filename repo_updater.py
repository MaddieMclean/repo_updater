import subprocess
import argparse
import os


def git(cmd):
    return ['git'] + cmd.split()


def clone(repo):
    subprocess.call(git(f'clone https://github.com/steeleye/{repo}.git'))


def pull(repo):
    subprocess.call(git(f'-C {path}/{repo} pull'))


def process(action):
    with open(f'{path}/.gitignore', 'r') as repos:
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
    cmd = args.command
    process(command[cmd])


if __name__ == '__main__':
    command = {
        'clone': clone,
        'pull': pull
    }
    path = os.getcwd()
    main()
