# Generated by Django 3.2.9 on 2022-01-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='auctions.Listings'),
        ),
    ]
