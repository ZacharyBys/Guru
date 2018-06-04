"""
Searches for command line errors and gives you the best answer from github
"""
from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='bughelper',
    version='0.1.0',
    url='https://github.com/ZacharyBys/BugHelper',
    license='BSD',
    author='Zachary Bys',
    author_email='zachary.bys@gmail.com',
    description='Searches for command line errors and gives you the best answer from github',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    entry_points={
        'console_scripts': [
            'bughelper = bughelper.cli:main',
        ],
    },
)
