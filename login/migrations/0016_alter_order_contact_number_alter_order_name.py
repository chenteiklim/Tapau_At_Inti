# Generated by Django 4.0.1 on 2022-02-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_alter_comment_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Contact_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]