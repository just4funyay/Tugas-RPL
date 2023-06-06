# Generated by Django 4.2 on 2023-05-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0002_alter_fundmodel_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundmodel',
            name='Kategori',
        ),
        migrations.AlterField(
            model_name='fundmodel',
            name='Jumlah',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fundmodel',
            name='kategori',
            field=models.TextField(choices=[('Pendapatan', 'Pendapatan'), ('Pengeluaran', 'Pengeluaran')], default='Pendapatan'),
        ),
    ]
