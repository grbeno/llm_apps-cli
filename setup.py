from setuptools import setup

setup(
    name="langapp",
    version="1.0",
    packages=["langapp"],
    entry_points={
        "console_scripts": ["langapp = langapp.__main__:main"],
    },
    description="Script to process model and role",
    author="grbeno",
    url="Project URL",
    python_requires=">=3.11.5",
)