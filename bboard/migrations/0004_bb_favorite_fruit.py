# Generated by Django 3.2.2 on 2021-06-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_fast_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='favorite_fruit',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
