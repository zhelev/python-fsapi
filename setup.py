# pylint: disable=invalid-name, exec-used
"""Setup fsapi package."""
from __future__ import absolute_import
import sys
import os
from setuptools import setup, find_packages
# import subprocess
sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# to deploy to pip, please use
# make pythonpack
# python setup.py register sdist upload
# and be sure to test it firstly using "python setup.py register sdist upload -r pypitest"
setup(name='fsapi',
      version='0.0.1',
      description=open(os.path.join(CURRENT_DIR, 'README.md')).read(),
      install_requires=['requests','lxml'],
      maintainer='Krasimir Zhelev',
      maintainer_email='krasimir.zhelev@gmail.com',
      zip_safe=False,
      packages=['fsapi'], #find_packages(),
      include_package_data=True,
      download_url = 'https://github.com/zhelev/python-fsapi/archive/master.zip',
      url='https://github.com/zhelev/python-fsapi.git',
      keywords = ['fsapi', 'frontier silicon'],
)
