from setuptools import setup, find_packages


__version__ = "0.0.1"
NAME = "transparent_qat-template"

setup(
    name=NAME,
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "pyscc>=0.0.2"
    ]
)
