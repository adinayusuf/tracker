# Generated by Django 4.0.5 on 2022-07-07 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=40, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Время изменения')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Описание')),
                ('text', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Текст')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.type')),
            ],
            options={
                'verbose_name': 'Описание',
                'verbose_name_plural': 'Описания',
                'db_table': 'to_do_lists',
            },
        ),
    ]
