import os
from celery import Celery
from celery.schedules import crontab
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilim.settings')

app = Celery('bilim')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def send_beat_email(email):
    send_mail(
        'Task',
        'Your task is done',
        'djangobeket@gmail.com',
        [email],
        fail_silently=False
    )
# app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     # 'add-every-monday-morning': {
#     #     'task': 'Place.tasks.offline_tasks',
#     #     'schedule': crontab(minute='*')
#     # },
#     # 'check-every-day-active-packet': {
#     #     'task': 'Place.tasks.check_activation_packet',
#     #     'schedule': crontab(hour=10, minute=59)
#     # }
# }