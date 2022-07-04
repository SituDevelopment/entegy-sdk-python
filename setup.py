from setuptools import setup

setup(
    name='entegywrapper',
    version='0.1.0',    
    description='A Python 3.10 wrapper for the Entegy API',
    url='https://github.com/SituDevelopment/python3-entegy-API-wrapper',
    author='Cameron Jensen',
    author_email='cameron@situ.com.au',
    license='BSD 2-clause',
    packages=['entegywrapper'],
    install_requires=['requests'                    
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
    ],
)