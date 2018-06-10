from setuptools import setup

setup(
    name='BooksServiceTransaction',
    packages=['transaction'],
    version="0.0.1",
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-classful'
    ],

    author="Thomas Ruggeri",
    author_email="thomaspublicext@gmail.com",
)
