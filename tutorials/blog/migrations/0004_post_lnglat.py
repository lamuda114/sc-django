# Generated by Django 2.0.6 on 2018-06-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]