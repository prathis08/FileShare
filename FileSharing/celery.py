from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FileSharing.settings')



app = Celery('FileSharing')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'delete_File': {
        'task': 'core.tasks.delete_File',
        'schedule': crontab(minute='*/60'),
    },
}


@app.task(bind = True)
def debug (self):
    return (f'Request : {self.request!r}')