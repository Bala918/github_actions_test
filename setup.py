from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in github_actions_test/__init__.py
from github_actions_test import __version__ as version

setup(
	name="github_actions_test",
	version=version,
	description="Test",
	author="Test",
	author_email="test@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
