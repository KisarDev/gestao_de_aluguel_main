# Generated by Django 4.2.7 on 2023-12-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoAluguel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='adiantamento',
            field=models.JSONField(blank=True, default={'dia_do_adiantamento': '00/00/0000', 'valor_do_adiantamento': 0.0}, null=True),
        ),
    ]
