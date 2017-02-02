"""
Setup file for the fsapi package
"""
from distutils.core import setup

setup(name='fsapi',
      version='0.0.4',
      description='Implementation of the Frontier Silicon API for python',
      # install_requires=['requests','lxml'],
      author='Krasimir Zhelev',
      author_email='krasimir.zhelev@gmail.com',
      packages=['fsapi'],
      keywords='fsapi frontier silicon',
      license='Apache 2',
      download_url='https://github.com/zhelev/python-fsapi/archive/0.0.3.zip',
      url='https://github.com/zhelev/python-fsapi.git')
