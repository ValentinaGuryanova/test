# Generated by Django 5.0.2 on 2024-02-25 16:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование продукта')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Модель продукта')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название поставщика')),
                ('level', models.IntegerField(choices=[(0, '0 - Завод'), (1, '1 - Розничная сеть'), (2, '2 - Индивидуальный предприниматель')], verbose_name='Уровень поставщика')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='electronic.contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'поставщик',
                'verbose_name_plural': 'поставщики',
            },
        ),
        migrations.CreateModel(
            name='NetWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название сети')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность поставщику')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='electronic.contact', verbose_name='Контакт')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='electronic.product', verbose_name='Продукт')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='electronic.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'звено сети',
                'verbose_name_plural': 'звенья сети',
            },
        ),
    ]
