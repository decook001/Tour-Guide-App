# Generated by Django 2.2.6 on 2019-11-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, null=True)),
                ('mobile', models.IntegerField()),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='GuidePhoto')),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('rent', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuideAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avail_from', models.DateField()),
                ('avail_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GuideBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_from', models.DateField()),
                ('book_to', models.DateField()),
                ('total_rent', models.FloatField()),
                ('booking_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
