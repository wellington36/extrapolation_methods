from setuptools import setup, find_packages

VERSION = '2.1.0'
DESCRIPTION = 'Extrapolation methods to real series'

# Setting up
setup(
    name="extrapolation",
    version=VERSION,
    author="Wellington Silva",
    author_email="<wellington.71319@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url="https://github.com/wellington36/extrapolation_methods",
    license='MIT',
    packages=find_packages(),
    install_requires=['mpmath'],
    keywords=['python', 'series', 'extrapolation', 'numerical-analysis']
)
