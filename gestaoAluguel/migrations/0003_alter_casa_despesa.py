# Generated by Django 4.2.9 on 2024-02-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0004_remove_despesa_nome_despesa_despesa_casa_and_more'),
        ('gestaoAluguel', '0002_morador_alter_casa_despesa_alter_casa_representante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='despesa',
            field=models.ManyToManyField(blank=True, related_name='casa_despesa', to='despesas.despesa'),
        ),
    ]
