# Generated by Django 3.2.8 on 2021-10-27 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_language_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['book']},
        ),
    ]
