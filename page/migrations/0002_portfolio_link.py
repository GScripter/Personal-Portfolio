# Generated by Django 3.2.8 on 2021-10-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
