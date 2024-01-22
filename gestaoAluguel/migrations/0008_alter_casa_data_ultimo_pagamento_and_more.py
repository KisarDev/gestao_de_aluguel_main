# Generated by Django 4.2.7 on 2024-01-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoAluguel', '0007_remove_contrato_inquilino_delete_mesrendimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='data_ultimo_pagamento',
            field=models.DateField(verbose_name='data_ultimo_pagamento'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='data_vencimento_aluguel',
            field=models.DateField(verbose_name='data_vencimento_aluguel'),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='rg',
            field=models.CharField(max_length=10, unique=True, verbose_name='RG'),
        ),
    ]
