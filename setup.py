from setuptools import setup, find_packages

setup(
    name="super_simple_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer"
    ],
    entry_points={
        "console_scripts": [
            "cli=super_simple_package.cli:app",
        ],
    },
)
