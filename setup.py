import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secmmf",
    version="0.0.1",
    author="Yangjue Han",
    author_email="yangjue.han20@gmail.com",
    description="Python scraper for SEC N-MFP2 filings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yj1990/sec_mmf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
