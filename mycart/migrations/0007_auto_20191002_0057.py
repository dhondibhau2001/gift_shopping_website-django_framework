# Generated by Django 2.2.4 on 2019-10-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0006_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('babygift', 'BABYGIFT'), ('birthdaygift', 'BIRTHDAYGIFT'), ('accentsgift', 'ACCENTSGIFT'), ('cristamgift', 'CRISTAMGIFT'), ('toysgift', 'TOYSGIFT'), ('valentinegift', 'VALENTINEGIFT'), ('artificialgift', 'ARTIFICIALGIFT'), ('giftforher', 'GIFTFORHER'), ('giftforhim', 'GIFTFORHIM')], default='babygift', max_length=100),
        ),
    ]
