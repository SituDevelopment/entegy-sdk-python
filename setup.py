from setuptools import setup

setup(
    name="entegywrapper",
    version="0.1.10",
    description="A Python 3.10 wrapper for the Entegy API",
    url="https://github.com/SituDevelopment/python3-entegy-API-wrapper",
    author="Cameron Jensen",
    author_email="cameron@situ.com.au",
    license="BSD 2-clause",
    packages=[
        "entegywrapper",
        "entegywrapper/Content",
        "entegywrapper/Notification",
        "entegywrapper/Plugins",
        "entegywrapper/Points",
        "entegywrapper/Profiles",
    ],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
