import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    license_txt = fh.read()

setuptools.setup(
    name="lzutf8",
    version="0.1",
    author="b-01",
    description="Python implementation of lzutf8.js by rotemdan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/b-01/lzutf8.py",
    packages=setuptools.find_packages(),
    license=license_txt,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)