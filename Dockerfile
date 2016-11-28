FROM python:2.7

RUN rm -rf /MyGraphite
RUN mkdir /MyGraphite
WORKDIR /MyGraphite
ADD . /MyGraphite/
RUN ./uranium build


ENV PYTHONPATH /MyGraphite/webapp
CMD ./bin/django-admin.py migrate --settings=graphite.settings --run-syncdb
