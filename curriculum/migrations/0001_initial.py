# Generated by Django 3.2.9 on 2021-11-20 00:28

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
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='standards/')),
                ('description', models.TextField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, upload_to='subjects/')),
                ('description', models.TextField(blank=True, max_length=200)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='curriculum.standard')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('chapter_no', models.PositiveSmallIntegerField(verbose_name='chapter_no.')),
                ('video', models.FileField(blank=True, null=True, upload_to='lessons/', verbose_name='Video')),
                ('ppt', models.FileField(blank=True, null=True, upload_to='ppt/', verbose_name='Presentation')),
                ('notes', models.FileField(blank=True, upload_to='notes/', verbose_name='Notes')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='curriculum.subject')),
            ],
            options={
                'ordering': ['chapter_no'],
            },
        ),
    ]
