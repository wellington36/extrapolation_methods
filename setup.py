from setuptools import setup, find_packages
import codecs
import os

VERSION = '2.0.0'
DESCRIPTION = 'Acceleration methods to real series'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="acceleration",
    version=VERSION,
    author="Wellington Silva",
    author_email="<wellington.71319@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    license='MIT',
    packages=find_packages(),
    install_requires=open('requirements.txt').read(),
    keywords=['python', 'extrapolation', 'numerical-analysis']
)
