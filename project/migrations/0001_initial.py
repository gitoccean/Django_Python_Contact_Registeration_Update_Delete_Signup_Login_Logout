# Generated by Django 4.2.3 on 2023-07-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Confirm_Password', models.CharField(max_length=30)),
            ],
        ),
    ]
