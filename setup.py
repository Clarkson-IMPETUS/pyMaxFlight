import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyMaxFlight-IMPETUS",
    version="0.1.1",
    author="Joseph Judge",
    author_email="judgejc@clarkson.edu",
    description="Python module for interfacing with and processing data from the MaxFlight Motion Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Clarkson-IMPETUS/pyMaxFlight",
    project_urls={
        "Bug Tracker": "https://github.com/Clarkson-IMPETUS/pyMaxFlight/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data= True,
    install_requires=[],
    package_data={
        '': ['Visualization/models/coloredCube.glb']
    }
)
