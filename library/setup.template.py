__version__ = "0.0.1"
NAME = "transparent_qat-template"

from setuptools import setup, find_packages

setup(
    name=NAME,
    version=__version__,
    packages=find_packages(),
    namespace_packages=["template"],
    install_requires=[
        "selenium==3.0.0b3",
        "pyvirtualdisplay",
    ]
)
