import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-material-admin",
    version="0.0.1",
    author="Anton Maistrenko",
    author_email="it2015maistrenko@gmail.com",
    description="Material Design For Django Administration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaistrenkoAnton/django-material-admin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        'Framework :: Django 2.0',
        'Framework :: Django 2.1',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)