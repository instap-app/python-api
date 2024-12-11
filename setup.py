from setuptools import setup, find_packages

setup(
    name="instapi",
    version="0.1.0",
    author="Instap",
    author_email="api@instap.app",
    description="Instap API for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/instap-app/python-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "slugify",
    ],
)