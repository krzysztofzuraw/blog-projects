from __future__ import absolute_import

from celery import Celery

app = Celery('transcoder',
             broker='amqp://admin:admin@localhost//',
             include=['taskapp.tasks'])

if __name__ == '__main__':
    app.start()
