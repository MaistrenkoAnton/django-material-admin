import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="django-material-admin",
    version="0.0.7",
    packages=find_packages(),
    author="Anton Maistrenko",
    include_package_data=True,
    author_email="it2015maistrenko@gmail.com",
    description="Material Design For Django Administration",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MaistrenkoAnton/django-material-admin",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
