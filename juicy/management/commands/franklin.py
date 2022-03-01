from re import L
from webbrowser import get
# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from juicy.models import Car

class Command(BaseCommand):
    help = "Db random car generator"

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='The amount of car to creeate')
        #SOME NEW TYPES UNDER
        #nargs="+"
        #parser.add_argument('-a', '--admin', action='store_true', help='The amount of car to creeate' )
    def handle(self, *args, **kwargs):
        qty = kwargs['qty']
        #IF LOGIC FOR COMMAND
        # admin = kwargs["admin"]
        # if admin:
        #     asdfasd
        for i in range(qty):
            title = get_random_string(10)
            model = get_random_string(10)
            age = 5
            Car.objects.create(title=title, model=model, age=age)
