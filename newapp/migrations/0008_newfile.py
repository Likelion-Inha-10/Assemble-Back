# Generated by Django 4.0.6 on 2022-07-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_remove_user_groups_user_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfile', models.FileField(upload_to='')),
            ],
        ),
    ]
