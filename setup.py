from setuptools import setup

setup(
    name='hivery',
    packages=['hivery', 'hivery.tests', 'hivery.resources'],
    author='exis',
    python_requires='>=3.7',
    install_requires=[
        'flask',
        'djangorestframework',
        'requests',
    ]
)
