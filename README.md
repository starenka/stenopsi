# stenopsi

Attempt to scrape, parse and index all stenographic records from Czech Parliament.
The goal is to provide structured records in language agnostic format you can use to feed your database (f.e Elastic).

## installation

Make new virtualenv with python 2 and install all requirements:

    virtualenv .env
    source .env/bin/activate
    pip install -r requirements.pip

For your convenience check [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/).

## usage

With virtualenv activated (`source .env/bin/activate`) all actions should be accesiable via Makefile:

 - to get all needed data, do `make download`
 - to get parsed data as json, use `make parse`
 - (wip)

## roadmap

 - get all available data [ok]
 - parse it [almost]
 - provide dumps [ok]
 - webapp to search within the data
