from setuptools import setup, find_packages

from baseplate.integration.thrift.command import ThriftBuildPyCommand


setup(
    name="{{ cookiecutter.project_name }}",
    packages=find_packages(),
    install_requires=[
        "baseplate",
    ],
    tests_require=[
        "nose",
        "coverage",
    ],
    cmdclass={
        "build_py": ThriftBuildPyCommand,
    },
)
