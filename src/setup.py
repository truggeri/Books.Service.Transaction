from setuptools import setup

setup(
    name='BooksServiceTransaction',
    packages=['BooksServiceTransaction'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-classful'
    ]
)
