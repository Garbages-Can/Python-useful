#!/usr/bin/env python3
from pip._internal import get_installed_distributions
from subprocess import call

for dist in get_installed_distributions():
    call('pip3 install --upgrade ' + dist.project_name, shell=True)
