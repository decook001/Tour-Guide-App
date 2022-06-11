# Generated by Django 2.2.6 on 2019-11-18 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.FloatField(default=None, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['owner'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='FoodPhoto')),
                ('price', models.FloatField()),
                ('person', models.PositiveIntegerField(blank=True, default=1)),
                ('available_at_time', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('All Time', 'All Time')], max_length=255)),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'ordering': ['restaurant'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.FloatField()),
                ('order_time', models.DateTimeField()),
                ('status', models.CharField(max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-order_time'],
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.IntegerField(blank=True, default=None, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='RestaurantPhoto')),
                ('city', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.City')),
                ('country', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Country')),
                ('user_detail', models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='homepage.UserDetail')),
            ],
            options={
                'ordering': ['user_detail'],
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Food')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Order')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Cart')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Food')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='restaurant',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
    ]
