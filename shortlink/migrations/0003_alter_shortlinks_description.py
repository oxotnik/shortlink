# Generated by Django 4.0.1 on 2022-01-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0002_alter_shortlinks_date_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlinks',
            name='description',
            field=models.TextField(default=None, null=True, verbose_name='Описание'),
        ),
    ]