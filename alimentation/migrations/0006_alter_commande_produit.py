# Generated by Django 4.0.3 on 2022-08-10 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alimentation', '0005_rename_id_commande_commande_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alimentation.produit'),
        ),
    ]