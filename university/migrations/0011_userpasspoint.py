# Generated by Django 3.2 on 2021-12-18 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('university', '0010_motivation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPassPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=50, null=True)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faculty_user_pass', to='university.faculty', verbose_name='Faculty')),
                ('specialty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialty_user_pass', to='university.specialty', verbose_name='Specialty')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_user_pass', to='university.university', verbose_name='University')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]