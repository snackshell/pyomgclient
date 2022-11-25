from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.1.0"
setup(
    name="pyomgclient",
    version=VERSION,
    author="Team XProjects",
    description="a python omegle client",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'colorama'],
    keywords=['python', 'omegle', 'XProjects', 'TheXProjects', 'client', 'omegleclient', 'pyomgclient', 'omgclient', 'pythonomengleclient'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
