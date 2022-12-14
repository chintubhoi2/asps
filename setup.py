from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."
def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_files:
        requirement_list = requirement_files.readline()
    requirement_list = [requirement_list.replace("\n","") for requirement_name in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_files

setup(
    name = "sensor",
    version = "0.0.1",
    author = "ved",
    author_email = "bhoi.chintu@gmail.com",
    package = find_package(),
    install_requires = get_requirements(),
)