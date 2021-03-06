# Generated by Django 4.0.4 on 2022-04-14 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('campanyemail', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(choices=[('RWANDA', 'rwanda'), ('Uganda', 'uganda'), ('BURUNDI', 'burundi'), ('CONGO', 'congo')], default='RWANDA', max_length=25)),
                ('category', models.CharField(choices=[('VORCANOES', 'vorcanoes'), ('HOTEL', 'hotel'), ('HILLS', 'hills')], default='VORCANOES', max_length=25)),
                ('image', models.ImageField(upload_to='product_image')),
                ('payment', models.CharField(choices=[('FREE', 'free'), ('NOT FREE', 'not free')], default='FREE', max_length=25)),
                ('description', models.CharField(max_length=10000)),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
