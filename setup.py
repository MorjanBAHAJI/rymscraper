import setuptools
import rymscraper

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rymscraper",
    version=rymscraper.__version__,
    author="dbeley",
    author_email="dbeley@protonmail.com",
    description="Rateyourmusic scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbeley/rymscraper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        "async-generator==1.10",
        "attrs==21.4.0",
        "beautifulsoup4==4.11.1",
        "bs4==0.0.1",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "charset-normalizer==2.0.12",
        "cryptography==37.0.2",
        "h11==0.13.0",
        "idna==3.3",
        "lxml==4.8.0",
        "numpy==1.22.3",
        "outcome==1.1.0",
        "pandas==1.4.2",
        "pycparser==2.21",
        "pyopenssl==22.0.0",
        "pysocks==1.7.1",
        "python-dateutil==2.8.2",
        "pytz==2022.1",
        "requests==2.27.1",
        "selenium==4.1.5",
        "six==1.16.0",
        "sniffio==1.2.0",
        "sortedcontainers==2.4.0",
        "soupsieve==2.3.2.post1",
        "tqdm==4.64.0",
        "trio==0.20.0",
        "trio-websocket==0.9.2",
        "urllib3==1.26.9",
        "wsproto==1.1.0",
        "rapidfuzz",
    ],
)
