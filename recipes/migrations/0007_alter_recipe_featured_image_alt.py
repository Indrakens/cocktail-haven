# Generated by Django 3.2.22 on 2023-11-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20231109_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='featured_image_alt',
            field=models.CharField(default='green-lime-cocktail', max_length=100),
        ),
    ]