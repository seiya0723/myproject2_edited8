# Generated by Django 2.2.6 on 2021-05-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_topic_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='salary',
            field=models.IntegerField(null=True, verbose_name='収入'),
        ),
        migrations.AddField(
            model_name='topic',
            name='spending',
            field=models.IntegerField(null=True, verbose_name='支出'),
        ),
    ]
