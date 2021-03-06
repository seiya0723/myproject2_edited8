# Generated by Django 3.1.2 on 2021-06-04 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_auto_20210522_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='salary',
            new_name='income',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='price',
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bbs.category', verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='comment',
            field=models.CharField(blank=True, max_length=2000, verbose_name='コメント'),
        ),
    ]
