from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Pedro Santos(luksprkz)",
    author_email="pvitor2013@gmail.com",
    description="Package created as a project for Geração Tech Unimed-BH - Ciência de Dados Bootcamp",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luksprkz"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)