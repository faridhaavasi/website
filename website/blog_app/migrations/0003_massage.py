# Generated by Django 4.0.6 on 2022-07-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_article_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
