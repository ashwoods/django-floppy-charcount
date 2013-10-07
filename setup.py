import os
from setuptools import setup, find_packages

from floppy_charcount import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='floppy_charcount',
    version=".".join(map(str, VERSION)),
    description='A django fields/widgets that displays a normal text input with a remaining character count beside it.',
    long_description=readme,
    author="Ashley Camba Garrido",
    author_email='ashwoods@gmail.com',
    url='https://github.com/ashwoods/django-floppy-charcount',
    packages=find_packages(),
    package_data={
        'floppy_charcount': [
        ],
    },
)
