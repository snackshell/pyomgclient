from setuptools import setup, find_packages

setup(
    name='pyomgclient',
    version='1.0.0',
    description='python omegle client',
    long_description="README.md",
    author='Team XProjects',
    url='https://github.com/TheXProjects/pyomgclient',
    license="LICENSE",
    packages=find_packages(exclude=('tests', 'docs'))
)
