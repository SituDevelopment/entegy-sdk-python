from setuptools import setup

setup(
    name="entegywrapper",
    version="1.0.2",
    description="A Python 3.10 wrapper for the Entegy API",
    url="https://github.com/SituDevelopment/python3-entegy-API-wrapper",
    author="William Sawyer",
    author_email="william@situ.com.au",
    license="BSD 2-clause",
    packages=[
        "entegywrapper",
        "entegywrapper/Points",
        "entegywrapper/Content",
        "entegywrapper/Profiles",
        "entegywrapper/Plugins",
        "entegywrapper/Notification",
    ],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
