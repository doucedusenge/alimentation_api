# Generated by Django 4.0.3 on 2022-08-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentation', '0002_alter_produit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vente',
            name='produit',
            field=models.CharField(max_length=50),
        ),
    ]
