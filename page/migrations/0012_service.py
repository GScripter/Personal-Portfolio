# Generated by Django 3.2.8 on 2021-10-28 23:49

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_auto_20211028_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('icon', models.FileField(upload_to='icons')),
                ('alt', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
