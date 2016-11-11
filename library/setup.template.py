__version__ = "0.0.1"
NAME = "transparent_qat-template"

from setuptools import setup

setup(
    name=NAME,
    version=__version__,
    packages=["transparent_qat"],
    namespace_packages=["transparent_qat"],
    install_requires=[
        "selenium==3.0.0b3",
        "pyvirtualdisplay",
    ]
)
