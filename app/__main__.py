import argparse
import logging
import sys
import os

from kubernetes import client, config
#from .watcher import *

import subprocess


logger = logging.getLogger('main')
logging.basicConfig(level=logging.INFO)

PARSER = argparse.ArgumentParser()
PARSER.add_argument("--tester")

def main():

    helm = subprocess.Popen(['helm','list'])
    helm = subprocess.run(['helm','install --upgrade'])


if __name__ == '__main__':
    main()
