# Generated by Django 4.2.7 on 2024-01-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0002_remove_despesas_casa_despesas_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesas',
            name='identificador',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
