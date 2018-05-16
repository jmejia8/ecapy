#!/usr/bin/env python3
from setuptools import setup, Extension
from setuptools.command.install import install
from codecs import open
import subprocess
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class Installer(install):
    def run(self):
        command = "git clone https://github.com/jmejia8/eca"
        process = subprocess.Popen(command, shell=True, cwd="deps")
        process.wait()

        command = "make && mv eca.so ../../bin/eca.so"
        process = subprocess.Popen(command, shell=True, cwd="deps/eca")
        process.wait()
        
        install.run(self)

setup(
    name='ecapy',
    description='Evolutionary Centers Algorithm: Module for Python coded in C',
    url='https://github.com/jmejia8/ecapy',
    version='0.0.1',
    license='MIT',

    long_description=long_description,

    author='Jesus Mejia',
    author_email='jesusmejded@gmail.com',

    classifiers=[  
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='optimization evolutionary metaheuristic',

    packages=['eca'],

    dependency_links=['https://github.com/jmejia8/eca/archive/master.zip'],
    
    extras_require={  
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    cmdclass={'install': Installer},
    include_package_data=True,

    project_urls={  
        'Bug Reports': 'https://github.com/jmejia8/ecapy/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/jmejia8/ecapy/',
    },
)