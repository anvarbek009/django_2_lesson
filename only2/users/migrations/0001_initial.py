# Generated by Django 5.0.4 on 2024-04-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('user_address', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=100)),
            ],
        ),
    ]