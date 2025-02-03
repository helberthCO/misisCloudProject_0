from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "psycopg2-binary",
        "pyjwt",
        "passlib[bcrypt]",
        "gunicorn",
        "python-jose",
        "python-multipart",
        "uvicorn",
        "python-dotenv",
    ],
)