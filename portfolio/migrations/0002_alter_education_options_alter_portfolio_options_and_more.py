# Generated by Django 4.1.7 on 2023-02-19 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'education'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'portfolio'},
        ),
        migrations.RenameField(
            model_name='education',
            old_name='desc',
            new_name='description',
        ),
    ]
