# Generated by Django 3.0.4 on 2020-11-26 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name_plural': 'Species'},
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='api.Location'),
        ),
    ]
