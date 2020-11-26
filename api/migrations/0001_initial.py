# Generated by Django 3.0.4 on 2020-11-26 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('climate', models.CharField(max_length=100)),
                ('terrain', models.CharField(max_length=100)),
                ('surface_water', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('eye_color', models.CharField(max_length=50)),
                ('hair_color', models.CharField(max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='api.Species')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species', to='api.Species')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('original_title', models.CharField(max_length=255)),
                ('original_title_romanised', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('direction', models.CharField(max_length=255)),
                ('producer', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('people', models.ManyToManyField(to='api.Person')),
            ],
        ),
    ]
