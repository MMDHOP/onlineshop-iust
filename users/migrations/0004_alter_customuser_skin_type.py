# Generated by Django 5.2.4 on 2025-07-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_skin_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='skin_type',
            field=models.CharField(choices=[('dry', 'dry'), ('oily', 'oily'), ('combintion', 'combintaion'), ('sensitive', 'sensitive')], default='oily', max_length=10),
        ),
    ]
