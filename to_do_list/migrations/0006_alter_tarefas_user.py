# Generated by Django 5.0.1 on 2024-02-20 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0005_alter_tarefas_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='user',
            field=models.TextField(max_length=100),
        ),
    ]
