from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi[all]',
        'aiohttp',
        'sqlalchemy',
        'python-jose[cryptography]',
        'passlib[bcrypt]',
        'psycopg2-binary',
        'pydantic<2.0.0'
    ],
)
