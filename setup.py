from setuptools import find_packages,setup

def get_requirements():
    pass

setup(
    name = "sensor",
    version = "0.0.1",
    author = "ved",
    author_email = "bhoi.chintu@gmail.com",
    package = find_package(),
    install_requires = get_requirements(),


)