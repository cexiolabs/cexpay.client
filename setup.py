from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cexpay',
    version='2.0.1',
    description="A Python implementation of CEX Pay's APIs. See more https://developers.cexpay.io/.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cexiolabs/cexpay.client.python',
    author='Maksym Anurin',
    author_email='m.anurin@cexiolabs.com',
    license='Apache-2.0',
    packages=find_packages(exclude=["*test*"]),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
