# Generated by Django 4.0.2 on 2022-02-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(verbose_name='Expense date')),
                ('currency', models.CharField(choices=[('1', 'UAH'), ('2', 'USD')], max_length=3)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(verbose_name='Income date')),
                ('currency', models.CharField(choices=[('1', 'UAH'), ('2', 'USD')], max_length=3)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
