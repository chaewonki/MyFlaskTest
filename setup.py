# setup.py
from setuptools import setup, find_packages

setup(
    name="flaskapp",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask>=2.3.0',
        'Werkzeug>=2.3.0',
        'Jinja2>=3.1.2',
    ],
)