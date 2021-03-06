# Generated by Django 3.2.4 on 2021-06-05 20:34

from django.db import migrations
import imagekit.models.fields
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=user.models.CustomUser.user_directory_path),
        ),
    ]
