# Generated by Django 4.0.4 on 2022-05-09 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_alter_project_creator'),
        ('postapp', '0002_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post', to='projectapp.project'),
        ),
    ]