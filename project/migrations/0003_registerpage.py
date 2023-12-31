# Generated by Django 4.2.3 on 2023-07-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_signinpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField(max_length=15)),
                ('City', models.CharField(max_length=30)),
                ('Province', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
    ]
