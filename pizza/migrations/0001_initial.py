# Generated by Django 3.2.25 on 2024-10-08 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping1', models.CharField(max_length=100)),
                ('topping2', models.CharField(max_length=100)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.size')),
            ],
        ),
    ]
