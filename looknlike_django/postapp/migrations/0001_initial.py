# Generated by Django 4.0.4 on 2022-05-08 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='posts/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
