# Generated by Django 2.2.14 on 2021-09-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210907_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='decription',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]