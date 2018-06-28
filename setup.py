import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whats-py",
    version="0.0.5",
    author="Darsh Patel",
    author_email="darshkpatel@gmail.com",
    description="A minimal python library to interface with whatsappweb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darshkpatel/whats-py",
    packages=setuptools.find_packages(),
    install_requires=['selenium'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
