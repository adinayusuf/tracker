# Generated by Django 4.0.5 on 2022-08-13 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0013_project_members_alter_project_data_begin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('project_manager', 'Project Manager'), ('team_lead', 'Team Lead'), ('developer', 'Developer')], default='project_manager', max_length=250, verbose_name='Role')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectusers', to='webapp.project', verbose_name='Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprojects', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'projectuser',
                'unique_together': {('project', 'user')},
            },
        ),
    ]