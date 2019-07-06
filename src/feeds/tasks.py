from __future__ import absolute_import, unicode_literals
from celery import task
import random


@task()
def get_number():
    return ''.join(str(random.randrange(0,9)) for i in range(7))
     
