# Generated by Django 5.1.3 on 2024-12-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerfTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]
