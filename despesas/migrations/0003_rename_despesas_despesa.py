# Generated by Django 4.2.9 on 2024-02-06 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoAluguel', '0002_morador_alter_casa_despesa_alter_casa_representante_and_more'),
        ('despesas', '0002_despesas_pago'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Despesas',
            new_name='Despesa',
        ),
    ]
