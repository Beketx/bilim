from lib2to3.pytree import Base
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    
    #python help function - display documentation
    help = "It's Elon Musk giving name to baby"

    #calls when "python manage.py elon_musk"
    def handle(self, *args, **kwargs):
        baby_name = get_random_string(length=32)
        self.stdout.write(baby_name)