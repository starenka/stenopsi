# stenopsi

Attempt to scrape, parse and index all stenographic records from Czech Parliament.
The goal is to provide structured records in language agnostic format you can use to feed your database (f.e Elastic).

*So far it justs downloads all data for several past years. I'm working on parsing these files right now.*

## installation

Make new virtualenv with python 2 and install all requirements:

    virtualenv .env
    source .env/bin/activate
    pip install -r requirements.pip
    
For your convenience check [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/).

## usage

With virtualenv activated (`source .env/bin/activate`) all actions should be accesiable via Makefile:

 - to get all needed data, do `make download`
 - (wip)
 
## roadmap

 - get all available data
 - parse it
 - provide dumps
 - webapp to search within the data
 
