import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dante-pot-odds',
    version='0.1',
    # packages=find_packages('secretdiary'),
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Library to calculate pot odds in holdem',
    long_description=README,
    url='https://github.com/DanteOnline/dante-pot-odds',
    author='DanteOnline',
    author_email='iamdanteonline@gmail.com',
    keywords=['pot', 'odds', 'holdem', 'poker'],
    classifiers=[],
    # install_requires=['pycryptodome', 'pycryptodomex'],
    entry_points={
        'console_scripts': [
            'pot_odds = potodds.main:main',
        ]
    },
)
