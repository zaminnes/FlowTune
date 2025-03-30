from setuptools import setup, find_packages

setup(
    name="flowtune",
    version="1.2.0",
    author="zaminnes",
    author_email="your.email@example.com",
    description="Quantum-inspired resource loading DSL and SDK",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ['flowtune=flowtune.cli:main']
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
