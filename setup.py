from setuptools import setup, find_packages

setup(
    name = 'a8_jsonurl',
    version = '2.0.0',
    packages = find_packages(),
    install_requires = [],
    url = '',
    author = '',
    author_email = '',
    description = """
    A library for serialising and deserialising URL query strings which can represent
    hierarchical data structures which can also be represented as JSON.  
    
    This is convenient, for example, if you wish to have a web API which takes JSON 
    objects as a POST body, but which may also need to respond to GET requests for 
    which a more readable set of parameters would be appropriate.
    """,
    license = 'CC0',
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

