# Generated by Django 2.2.10 on 2020-04-12 09:33

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):
    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True),
        ),
    ]
