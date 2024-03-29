# Generated by Django 4.0.5 on 2022-08-13 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0012_project_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Projects'),
        ),
        migrations.AlterField(
            model_name='project',
            name='data_begin',
            field=models.DateField(max_length=20, verbose_name='Date begin'),
        ),
        migrations.AlterField(
            model_name='project',
            name='data_end',
            field=models.DateField(blank=True, max_length=20, null=True, verbose_name='Date end'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=40, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_tasks', to='webapp.project', verbose_name='Project'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_tasks', to='webapp.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='summary',
            field=models.CharField(max_length=15, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='type_tasks', to='webapp.type', verbose_name='Types'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(max_length=40, verbose_name='Type'),
        ),
    ]
