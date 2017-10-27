import subprocess
import argparse
import os


def git(cmd):
    return ['git'] + cmd.split()


def clone(repo):
    subprocess.call(git(
        f'clone https://github.com/steeleye/{repo} {path}/{repo}'))


def pull(repo):
    subprocess.call(git(f'-C {path}/{repo} checkout master'))
    subprocess.call(git(f'-C {path}/{repo} pull'))


def push(repo):
    subprocess.call(git(f'-C {path}/{repo} checkout master'))
    subprocess.call(git(f'-C {path}/{repo} checkout pypi-update'))
    subprocess.call(git(f'-C {path}/{repo} add .'))
    subprocess.call(git(f'-C {path}/{repo} commit -m "remove_pypi_secret"'))
    subprocess.call(git(f'-C {path}/{repo} push origin pypi-update'))


def process(action):
    with open(f'{path}/repositories.txt', 'r') as repos:
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
        'pull': pull,
        'push': push
    }
    path = "C:/Users/Mathew/PycharmProjects/SteelEye"
    main()
