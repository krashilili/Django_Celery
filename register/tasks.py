from __future__ import absolute_import, unicode_literals
import string
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task


@shared_task(name='create_random_user_accounts')
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return f'{str(total)} random users created with success!'



@shared_task
def add(x, y):
    return x+y


