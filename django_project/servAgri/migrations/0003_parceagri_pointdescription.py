# Generated by Django 2.2 on 2019-05-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servAgri', '0002_auto_20190528_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceagri',
            name='pointDescription',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]