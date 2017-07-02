blog-django-graphql-react-relay
-----------------------------

Quickstart
----------

To develop locally I'm using docker + docker compose. First make sure that you
installed docker by following these instructions: `link <https://docker.github.io/engine/installation/>`_.
Then run this command to run server & apply migrations.::

    $ make build
    $ make run
    $ make migrate
    $ make loaddata

Credits
-------

1. `Cookiecutter-django`_
2. `Cfgov-refresh`_
3. `Open-source-project-template`_

.. _Cookiecutter-django: https://github.com/pydanny/cookiecutter-django
.. _Cfgov-refresh: https://github.com/cfpb/cfgov-refresh
.. _Open-source-project-template: https://github.com/cfpb/open-source-project-template
