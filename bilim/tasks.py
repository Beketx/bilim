from celery import shared_task, chain, group
from django.core.mail import send_mail
from bilim.celery import app
from celery.utils.log import get_task_logger
import random, string

from juicy.models import Car, Computer, Mouse


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")

@app.task
def car_add_task():
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(20))
    age = random.randint(0,9)
    model = ''.join(random.choice(letters) for i in range(15))
    Car.objects.create(
        title=title,
        age=age,
        model=model
    )

@shared_task
def car_add():
    # car_add_task.delay()
    car_add_task.apply_async()

@app.task
def add(x, y):
    return x + y
"""
comany not tenant
goods get service not detail

When we chain tasks together, 
the second task will take the results of the first task as its first argument,
for example

from celery import chain

res = chain(add.s(1, 2), add.s(3)).apply_async() 

In the above example, you can notice the second task has only one argument , 
this is because the return value of the first task which in our example is
3 will be the first argument of the second task , the second task will now 
look like this
"""
@shared_task
def chain_trek():
    number = chain(add.s("THE CHAIN ","!!!!!!! "), add.s("WORRRRKSS")).apply_async()
    result = "$$$$$$$$$$$$$$$$$$$$$$&&&&&&&&& BEKET BEKET BEKET " + str(number)
    logger.info(result)

job = group([
        add.s("ONE THE GROUPPP ", "++++++++++++"),
        add.s("TWO THE GROUPPP ", "***************")
])

"""
Groups are used to execute tasks in parallel.
The group function takes in a list of signatures.
"""
@shared_task
def group_trek():
    result = job.apply_async()
    results = "READY - - - - - - " + result.get()
    logger.info(results)
    logger.info(result.ready())
    logger.info(result.successful())

#chord(header)(callback)
# callback = add.s()
# header = [add.s(2,2), add.s(4,4)]
# result = chord(header)(callback)
# result.get()

# @app.task
# def send_beat_email(email):
#         send_mail(
#             'Task',
#             'Your task is done',
#             'beketdjango@gmail.com',
#             [email],
#             fail_silently=False
#         )
