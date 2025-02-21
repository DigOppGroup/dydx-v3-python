from setuptools import setup, find_packages

LONG_DESCRIPTION = open('README.md', 'r').read()

REQUIREMENTS = [
    'dateparser',
    'ecdsa',
    'eth_keys',
    'eth-account',
    'mpmath',
    'pytest',
    'requests-mock',
    'requests',
    'setuptools',
    'sympy',
    'tox',
    'web3',
]

setup(
    name='dydx-v3-python',
    version='1.6.1',
    packages=find_packages(),
    package_data={
        'dydx3': [
            'abi/*.json',
            'starkex/starkex_resources/*.json',
        ],
    },
    description='dYdX Python REST API for Limit Orders',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/dydxprotocol/dydx-v3-python',
    author='dYdX Trading Inc.',
    license='Apache 2.0',
    author_email='contact@dydx.exchange',
    install_requires=REQUIREMENTS,
    keywords='dydx exchange rest api defi ethereum eth',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
