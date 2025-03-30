
from setuptools import setup, find_packages

setup(
    name="flowtune",
    version="1.1.0",
    author="zaminnes",
    author_email="your.email@example.com",
    description="Simplified Flowtune with automatic resource tracking",
    packages=find_packages(),
    install_requires=["requests"],
    url="https://github.com/zaminnes/flowtune",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)
