from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
import random, string
#cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from authorize.models import User
from bilim.tasks import send_beat_email, add, retry_test

from .models import Car, Computer, Mouse
from .serializers import CarSerializers, ComputerSerializers, MouseSerializers


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
"""
from django_redis import get_redis_connection
con = get_redis_connection("default")

frameworks = {'python':'Django','php':'Laravel','java':'Spring'} 
#Store them into redis hash.  
con.hmset('frameworks',frameworks)
True #successfully stored 

# retrieved number of items 
con.hlen('frameworks') 
3

#Get all values
con.hvals('frameworks')
[b'Django', b'Laravel', b'Spring']

 pipeline = con.pipeline()
  if feedlist:
     for post in feedlist:
         pipeline.execute_command('hgetall',post)
         #hgetall redis command to get all items of given hash key

Then call the execute() method on pipeline. It will return result back to result variable.

     result = pipeline.execute()

"""
class JuicyView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Computer.objects.all()
    
    # @cache_page(CACHE_TTL)
    def list(self, request):
        print(1)
        # x = add.delay(1,2)
        # send_beat_email.delay("beketsk@gmail.com")
        retry_test.delay(1)
        # print("################", x)
        # serializer = ComputerSerializers(self.queryset, many=True)
        # return Response(serializer.data)
        return Response()

    @action(detail=False, methods=['get'])
    def create_car(self, request):
        x = add.delay(1,2)
        for _ in range(1000):
            letters = string.ascii_lowercase
            title = ''.join(random.choice(letters) for i in range(20))
            age = random.randint(0,9)
            model = ''.join(random.choice(letters) for i in range(15))
            Car.objects.create(
                title=title,
                age=age,
                model=model
            )
        return Response({"Status": "good"})

    @action(detail=False, methods=['get'])
    def get_car(self, request):
        car = Car.objects.all()
        serializer = CarSerializers(car, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def create_computer(self, request):
        for _ in range(1000):
            letters = string.ascii_lowercase
            title = ''.join(random.choice(letters) for i in range(20))
            faculty = random.randint(1,5)
            specialty = random.randint(1,5)
            university = random.randint(2,3)
            user = random.randint(2,6)
            user = User.objects.get(id=user)
            Computer.objects.create(
                university_id = university,
                user = user,
                faculty_id = faculty,
                specialty_id = specialty,
                title = title
            )
        return Response({"Status": "good"})

    @action(detail=False, methods=['get'])
    def get_computer(self, request):
        #objects.prefetch
        #objects.select
        if 'computers' in cache:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            computer = cache.get('computer').data
            return Response(computer)
        else:
            print("############################")
            computer = Computer.objects.all()
            serializer = ComputerSerializers(computer, many=True)
            cache.set('computers', serializer, timeout=CACHE_TTL)
            return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def create_mouse(self, request):
        for _ in range(1000):
            letters = string.ascii_lowercase
            color = random.randint(2,1000)
            university = random.randint(2,3)
            type_in = ''.join(random.choice(letters) for i in range(15))
            Mouse.objects.create(
            university_id=university,
            type_in=type_in,
            color=color
            )
        return Response({"Status": "good"})
        
    @action(detail=False, methods=['get'])
    def get_mouse(self, request):
        #objects.prefetch
        #objects.select
        #annotate
        #aggregate
        mouse = Mouse.objects.all()
        serializer = MouseSerializers(mouse, many=True)
        return Response(serializer.data)
