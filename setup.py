import os
from setuptools import setup, find_packages
import hashdir

this_directory = os.path.abspath(os.path.dirname(__file__))


def read_file(path):
    with open(os.path.join(this_directory, path), encoding="utf-8") as f:
        return f.read()


long_description = read_file("README.md")

setup(
    name=hashdir.name,
    version=hashdir.__version__,
    url="https://github.com/fcivaner/hashdir",
    description=hashdir.description,
    description_content_type="text/markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="hash directory imohash md5",
    author="Fırat Civaner",
    author_email="fcivaner@gmail.com",
    license="MIT License",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["hashdir=hashdir.__main__:main"]},
    install_requires=["imohash"],
    setup_requires=["setuptools>=41.0.1", "wheel>=0.33.4"],
)
