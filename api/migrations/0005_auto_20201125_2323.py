# Generated by Django 3.0.4 on 2020-11-26 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201125_2321'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Character',
        ),
        migrations.AlterModelOptions(
            name='character',
            options={},
        ),
        migrations.RenameField(
            model_name='film',
            old_name='people',
            new_name='characters',
        ),
    ]