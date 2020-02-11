# Generated by Django 3.0.3 on 2020-02-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelid', models.CharField(max_length=255, verbose_name='channelid')),
                ('channeltitle', models.CharField(max_length=255, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelid', models.CharField(max_length=255, verbose_name='channelid')),
                ('videoid', models.CharField(max_length=255, verbose_name='videoid')),
                ('videotitle', models.CharField(max_length=255, verbose_name='videotitle')),
                ('channeltitle', models.CharField(max_length=255, verbose_name='channeltitle')),
                ('starttime', models.DateField(verbose_name='starttime')),
            ],
        ),
    ]