import subprocess
import os

import pandas as pd
import numpy as np

from datetime import datetime

import requests
import json

def get_johns_hopkins():
    ''' Get data by a git pull request, the source code has to be pulled first
        Result is stored in the predifined csv structure
    '''
    if os.path.exists('../data/raw/COVID-19/'):
        print('Repository found: Fetch the up to date data')
        git_pull = subprocess.Popen( "git pull" ,
                         cwd = os.path.dirname('../data/raw/COVID-19/' ),
                         shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE )
        (out, error) = git_pull.communicate()
    else:
        print('Repository not found. Fectch the entire repository')
        git_pull = subprocess.Popen( "git clone https://github.com/CSSEGISandData/COVID-19.git" ,
                         cwd = os.path.dirname('../data/raw/' ),
                         shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE )
        (out, error) = git_pull.communicate()




    print("Error : " + str(error))
    print("out : " + str(out))



if __name__ == '__main__':
    get_johns_hopkins()
