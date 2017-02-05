"""
Setup file for the fsapi package
"""
from setuptools import setup, find_packages

PACKAGES = find_packages(exclude=['tests', 'tests.*'])

REQUIRES = [
    'requests>=2,<3'
    'lxml>=3,<4'
]

PROJECT_CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries'
]



setup(name='fsapi',
      version='0.0.6',
      description='Implementation of the Frontier Silicon API for Python',
      author='Krasimir Zhelev',
      author_email='krasimir.zhelev@gmail.com',
      keywords='fsapi frontier silicon',
      license="Apache License 2.0",
      download_url='https://github.com/zhelev/python-fsapi/archive/0.0.6.zip',
      url='https://github.com/zhelev/python-fsapi.git',
      maintainer='Krasimir Zhelev',
      maintainer_email='krasimir.zhelev@gmail.com',
      zip_safe=True,
      include_package_data=True,
      packages=PACKAGES,
      platforms='any',
      install_requires=REQUIRES,
      classifiers=PROJECT_CLASSIFIERS,
     )
