# Generated by Django 4.2 on 2023-05-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО ученика\\студента')),
                ('social_status', models.CharField(max_length=200, verbose_name='Специальность\\Социальный статус')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('comment', models.TextField(max_length=500, verbose_name='Текст')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.teacher', verbose_name='Отзыв на учителя')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
