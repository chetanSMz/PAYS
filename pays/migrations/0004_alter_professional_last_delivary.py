# Generated by Django 4.0.8 on 2023-03-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0003_alter_user_professional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='Last_delivary',
            field=models.CharField(default='0000-00-00', max_length=100),
        ),
    ]
