# Generated by Django 4.0.4 on 2022-06-08 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_remove_homepage_subscribe_title_subscription_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagecards',
            options={'verbose_name': 'Home Page Course List', 'verbose_name_plural': 'Home Page Course List'},
        ),
    ]