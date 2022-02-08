from celery import shared_task
from django.core.mail import send_mail
from bilim.celery import app
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")

# @app.task
# def send_beat_email(email):
#         send_mail(
#             'Task',
#             'Your task is done',
#             'beketdjango@gmail.com',
#             [email],
#             fail_silently=False
#         )
