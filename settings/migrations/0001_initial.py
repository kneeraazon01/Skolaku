# Generated by Django 4.0.4 on 2022-05-06 19:35

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('whatsapp_no', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('usp_title', models.CharField(max_length=100)),
                ('bonus_title', models.CharField(max_length=100)),
                ('testmonial_title', models.CharField(max_length=100)),
                ('trainer_title', models.CharField(max_length=100)),
                ('subscribe_title', models.CharField(max_length=100)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('hero_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('featured_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('home_product_title', models.CharField(max_length=100, verbose_name='Home Product Title')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('card_title', models.CharField(max_length=100)),
                ('card_desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, default='', max_length=140)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('linkedin', models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='USP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(blank=True, max_length=100, null=True)),
                ('card_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('card_desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
