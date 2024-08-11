import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Lovely-102218034",
    version="1.0.1",
    description="It will find the topsis score of data to find the best module",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bansal9855/Topsis-Lovely-102218034",
    author="Lovely Bansal",
    author_email="admin@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=['pandas','numpy'],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)