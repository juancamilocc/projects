# Generated by Django 4.1.7 on 2023-03-28 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=4)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
