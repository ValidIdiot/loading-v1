from setuptools import setup, find_packages

setup(
    name="loading v1",
    version="0.1.0",
    author="Jerraf2p0",
    author_email="your_email@example.com",
    description="A module used to create loading bars.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ValidIdiot/loading-v1",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
