# Generated by Django 4.2.1 on 2023-05-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=260)),
            ],
        ),
    ]