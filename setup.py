import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyRMVtransport",
    version="0.0.8",
    author="cgtobi",
    author_email="cgtobi@gmail.com",
    description="Get transport information from opendata.rmv.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgtobi/PyRMVtransport",
    packages=setuptools.find_packages(exclude=('tests',)),
    install_requires=[
        'lxml',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
