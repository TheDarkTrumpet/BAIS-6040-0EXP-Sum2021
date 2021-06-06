import setuptools

setuptools.setup(
    name="AzureSync",
    version="0.0.1",
    author="David Thole",
    author_email="david@thedarktrumpet.com",
    description="An example project for uploading files into Azure.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)