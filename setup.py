from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in w2w/__init__.py
from w2w import __version__ as version

setup(
	name="w2w",
	version=version,
	description="Bio & E - Waste Management",
	author="Neveka Berl J",
	author_email="nevekaberyl@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
