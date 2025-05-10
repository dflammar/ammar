from django.db import migrations, models
import django.db.models.deletion
import core.models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.PositiveIntegerField(default=0, help_text='Video duration in seconds'),
        ),
        migrations.AddField(
            model_name='video',
            name='video_type',
            field=models.CharField(choices=[('upload', 'Uploaded Video'), ('youtube', 'YouTube Video')], default='upload', max_length=10),
        ),
        migrations.AddField(
            model_name='video',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(blank=True, help_text='YouTube video ID (automatically extracted from URL)', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_url',
            field=models.URLField(blank=True, help_text='YouTube video URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)', null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to=core.models.video_upload_path),
        ),
        migrations.AddField(
            model_name='videoview',
            name='completed',
            field=models.BooleanField(default=False, help_text='Whether the video was watched to completion'),
        ),
        migrations.AddField(
            model_name='videoview',
            name='device_type',
            field=models.CharField(blank=True, help_text='Device type (desktop, mobile, tablet)', max_length=20),
        ),
        migrations.AddField(
            model_name='videoview',
            name='watch_duration',
            field=models.PositiveIntegerField(default=0, help_text='Time watched in seconds'),
        ),
        migrations.AlterModelOptions(
            name='videoview',
            options={'ordering': ['-viewed_at']},
        ),
    ]
