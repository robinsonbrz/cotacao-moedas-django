# Generated by Django 4.0.5 on 2022-07-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao_grafico', '0005_alter_precos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precos',
            name='data',
            field=models.CharField(max_length=30),
        ),
    ]
