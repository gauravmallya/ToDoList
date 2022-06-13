# Generated by Django 4.0.5 on 2022-06-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('TaskID', models.AutoField(primary_key=True, serialize=False)),
                ('TaskName', models.CharField(max_length=200)),
                ('TaskCompletion', models.BooleanField()),
            ],
        ),
    ]