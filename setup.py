from setuptools import setup, find_packages
import os
from pathlib import Path
os.path.dirname(os.path.abspath('__file__'))
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



setup(
    name="demopackagepy",
    version="1.0",
    author="Mihaly Orsos",
    author_email="",
    description="Demo package",
    url="https://github.com/misrori/demopackagepy",
    license="MIT",
    install_requires=[],
    packages=find_packages()
)

