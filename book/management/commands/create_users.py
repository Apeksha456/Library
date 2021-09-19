from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

# class Command(BaseCommand):
#     help = 'Create random users'

#     def add_arguments(self, parser):
#         parser.add_argument('total', type=int, help='Indicates the number of users to be created')

#     def handle(self, *args, **kwargs):
#         print(kwargs)     # {"total": 10}
#         total = kwargs['total']
#         for i in range(total):
#             s = get_random_string(5)
#             User.objects.create_user(username=s, email= s+"@gmail.com", password='123')



class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        total = kwargs['total']    # 10 - total
        prefix = kwargs['prefix']   # custom_user - prefix
        print(kwargs)

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()
            User.objects.create_user(username=username, email='', password='123')




