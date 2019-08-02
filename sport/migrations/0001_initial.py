# Generated by Django 2.2.3 on 2019-07-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('pseudo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
