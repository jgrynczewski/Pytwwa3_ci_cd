# Generated by Django 3.1 on 2020-08-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='category',
            field=models.CharField(choices=[('', '---------'), ('question', 'Pytanie'), ('answer', 'Odpowiedź'), ('other', 'Inne')], max_length=10),
        ),
    ]