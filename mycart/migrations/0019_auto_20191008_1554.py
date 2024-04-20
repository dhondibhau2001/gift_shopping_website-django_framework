# Generated by Django 2.2.4 on 2019-10-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0018_auto_20191008_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('babygift', 'BABYGIFT'), ('birthdaygift', 'BIRTHDAYGIFT'), ('accentsgift', 'ACCENTSGIFT'), ('cristamgift', 'CRISTAMGIFT'), ('toysgift', 'TOYSGIFT'), ('valentinegift', 'VALENTINEGIFT'), ('artificialgift', 'ARTIFICIALGIFT'), ('giftforher', 'GIFTFORHER'), ('giftforhim', 'GIFTFORHIM')], default='babygift', max_length=100),
        ),
    ]
