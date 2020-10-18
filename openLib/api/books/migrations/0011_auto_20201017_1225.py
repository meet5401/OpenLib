# Generated by Django 3.1.2 on 2020-10-17 06:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20201017_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='rating_book', to=settings.AUTH_USER_MODEL),
        ),
    ]