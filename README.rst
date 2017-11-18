Persefone
=========
|Pypi| |Travis|

Persefone is a Siren encoder that uses ujson to generate Siren documents
efficiently.

Usually such encoders work with JSON, so you convert your data to JSON and pass
it to the encoder.

The idea behind persefone is to provide a perfomant Siren encoder by removing
the JSON conversion step: you pass your data as provided by your ORM and
persefone deals with that, returning JSON.


Supported orms and data structures
##################################

Persefone currently supports only peewee, but I plan to add support for other
ORMs and similar tools.res

Usage
#####

Install with pip::

    pip install persefone


Then::

    from persefone import Siren

    Siren(data, '/path', model=MyModel).encode() # returns Siren-valid JSON


If you have a list::

    Siren([item, ...], '/path', model=MyModel)

Pagination::

    Siren([item, ...], '/path', model=MyModel, total_items=100, current_page=2)


Contributing
############
Contributions and feedbacks are welcome. You can just open an issue.


.. |Pypi| image:: https://img.shields.io/pypi/v/persefone.svg?maxAge=3600&style=for-the-badge
   :target: https://pypi.python.org/pypi/persefone

.. |Travis| image:: https://img.shields.io/travis/Vesuvium/persefone.svg?maxAge=3600&style=for-the-badge
   :target: https://travis-ci.org/Vesuvium/persefone
