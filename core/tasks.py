from celery import shared_task
from .models import File
import os
from datetime import datetime, timedelta
FMT = '%H:%M:%S'
DFMT = '%Y-%M-%D'

@shared_task(bind = True)
def delete_File(self):
    yesterday = datetime.date.today() - datetime.timedelta(days = 1)
    # p = datetime.now() - timedelta(minutes = 5)
    file_to_be_deleted = File.objects.filter(uploaded_on__lt = yesterday)
    for f in file_to_be_deleted:
        os.remove(f.file.path)
        f.delete()
        return ("{} deleted ".format(f))