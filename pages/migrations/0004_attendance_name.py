# Generated by Django 3.0.6 on 2020-06-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_sqluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='name',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]