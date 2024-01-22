import random
import os, sys
import shutil

""" 
repo-list file should look like :
    https://github.com/username1/seatech-python-robotic.git 
    https://github.com/username2/seatech-python-robotic.git 
    https://github.com/username3/seatech-python-robotic.git
No trailing blank line !
"""

if __name__ == '__main__':

    REPO_FOLDER = 'repos'
    PICK_AMOUNT = 3
    CURRENT_FOLDER = os.getcwd()
    REPO_LIST_FILE = './repo-list'

    if not os.path.exists(REPO_LIST_FILE):
        print('No %s file !'%(REPO_LIST_FILE))
        sys.exit(-1)

    with open(REPO_LIST_FILE, 'r') as f:
        repos = f.read()

    repos = repos.split('\n')

    if os.path.exists(REPO_FOLDER):
        shutil.rmtree(REPO_FOLDER)

    os.mkdir(REPO_FOLDER)
    os.chdir(REPO_FOLDER)

    random_list = random.choices(repos, k=PICK_AMOUNT)

    for repo in repos:
        username = repo.split('/')[3]
        os.system('git clone %s %s'%(repo, username))
        # os.system('git clone %s'%(repo))

    os.chdir(CURRENT_FOLDER)