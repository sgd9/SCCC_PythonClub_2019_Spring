# Generated by Django 2.2 on 2019-06-02 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productdescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clubapp.Product'),
        ),
    ]
