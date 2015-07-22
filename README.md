
Thanks
======

This is the code of http://fixmystreet.irisnet.be project stand at https://github.com/CIRB/django-fixmystreet.

It is a fork of http://fixmystreet.ca (https://github.com/visiblegovernment/django-fixmystreet), thank you to them for providing this great project !

This project in place use Urbis for map, search and locate engine (http://geoserver.gis.irisnet.be/).


[![data model](https://raw.github.com/CIRB/django-fixmystreet/master/data-model.png)](http://fixmystreet.irisnetlab.be/admin/doc/)


Installation
============
First install docker and docker-compose.

```bash
$ git clone git@github.com:IMIO/django-fixmystreet.git
$ make docker-init
$ make docker-run
```

Variables
============

In deploy environment, settings are given by system environment variables.

Available variables:

```bash
ENV # environment that is running, supported values are local / dev / staging / production
MEDIA_ROOT # path to dynamic files upload location
GA_CODE # code Google Analytic

# database variables
DATABASE_ENGINE
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
DATABASE_PORT
DATABASE_HOST
```


Useful commands
===============

To generate po files, run the following command:

    $ make messages

For sample data set loading:

    $ env/bin/manage.py loaddata sample.json
    $ cp -Rf media/photos-sample/ media/photos/

    $ env/bin/manage.py testserver sample.json

    $ env/bin/manage.py dumpdata mainapp.Report mainapp.ReportUpdate mainapp.ReportSubscriber --format json --indent 2 > mainapp/fixtures/sample.json


To generate data model image:

    $ env/bin/manage.py graph_models fixmystreet -g -o data-model.png


Dump DB:

    pg_dump fixmystreet -U fixmystreet > fixmystreet_dump.sql

Import dump DB:

    dropdb fixmystreet -U postgres
    createdb --template=template_postgis fixmystreet -U postgres -O fixmystreet
    cat fixmystreet_dump.sql | psql -U fixmystreet
