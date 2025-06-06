# Generated by Django 5.2 on 2025-05-06 16:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_grade_students'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ar', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('bio_ar', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teacher_photos/')),
                ('specialization', models.CharField(blank=True, max_length=100)),
                ('specialization_ar', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('courses', models.ManyToManyField(blank=True, related_name='teachers', to='core.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TeacherReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(help_text='Rating from 1 to 5 stars', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_reviews', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.teacher')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('teacher', 'student')},
            },
        ),
    ]
