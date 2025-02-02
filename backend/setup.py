from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "fastapi-cors",
        "sqlalchemy",
        "psycopg2",
        "pyjwt",
        "passlib",
        "gunicorn",
        "python-jose",
        "python-multipart",
        "uvicorn",
    ],
)