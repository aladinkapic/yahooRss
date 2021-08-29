from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yahooRss.settings')

broker = 'sqla+postgresql://' + settings.DB_USERNAME + ':' + settings.DB_PASSWORD + '@' + settings.DB_HOST + '/' + settings.DB_DATABASE

app = Celery('yahooRss', broker=broker)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'test-task-v3': {
        'task': 'news.tasks.fetchData',
        'schedule': crontab(),
        # 'args'
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
