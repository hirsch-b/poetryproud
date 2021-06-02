# PeotryProud

PeotryProud is a project that queries different APIs to serv poetry built to promote internally Poetry for Python and its greatness.

Please do not run this sample in production.

## How to use it?

Poetry is required, [get poetry](https://python-poetry.org/), then clone this project.

### Running tests

`pytest` is used for unit testing and simple tests can be ran through poetry's virtual environment:

    poetry run pytest
    poetry run pycodestyle --ignore=E126,E127,E128,W503 poetryproud/

### Building

Building is as simple as typing:

    poetry build

It will create a `dist` folder with packages name according to the project name and version. The project that was built can be directly installed with `pip` by specifying the archive as so:

    pip install dist/poetryproud-0.1.0.tar.gz

### Importing

This sample code will return some poetry for your code:

    from poetryproud import haiku

    poem = haiku.get_random()
    print(poem["haiku"])

### Makefile

The `Makefile` contains some examples of other usages.

## Sources

PeotryProud proudly queries:

* https://poetrydb.org/
* https://haiku-json-db.herokuapp.com/
