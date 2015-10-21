#!/usr/bin/python

print("""Congrats! Your baseplate thrift project is ready to go!

Next steps:

Build it (this also generates code from your thrift interface)

    python setup.py build

Install it

    python setup.py develop --user

Start up the application

    baseplate-serve2 --debug example.ini

Any time you modify your .thrift file, you will need to re-run "setup.py build"
to re-generate the thrift code for your service.

Thrift comes with a built in client you can use from the command line for quick
testing. For example:

    python3 -m {{ cookiecutter.project_name }}.{{ cookiecutter.project_slug }}_thrift.remote -h localhost:9090 is_healthy

You can run your nascent test suite with:

    python setup.py nosetests

""")
