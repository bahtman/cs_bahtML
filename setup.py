#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 
    "geopandas",
    "pandas",
#    "awpy",
    "plotly",
    "Pillow",
    "scikit-learn"
]

test_requirements = [ ]

setup(
    author="Anton Baht",
    author_email='anton@baht.dk',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A util package for ML in CSGO",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cs_bahtml',
    name='cs_bahtml',
    packages=find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": [
            "radars/*.png",
            "radars/*.json",
            "sprites/*.png"
        ]
    },
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bahtman/cs_bahtml',
    version='0.1.0',
    zip_safe=False,
)
