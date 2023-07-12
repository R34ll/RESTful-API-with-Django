# Generated by Django 4.2.2 on 2023-07-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'Administrator'), (1, 'Developer'), (2, 'Design')], default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]