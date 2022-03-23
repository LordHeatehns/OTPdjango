from __future__ import absolute_import , unicode_literals  
import os 

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','otp.settings')

app = Celery('otp')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Bangkok')

app.config_from_object('django.conf:settings',namespace = 'CELERY')


app.autodiscover_tasks()



@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')