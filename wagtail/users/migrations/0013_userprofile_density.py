# Generated by Django 4.2.9 on 2024-04-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailusers", "0012_userprofile_theme"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="density",
            field=models.CharField(
                choices=[("default", "Default"), ("snug", "Snug")],
                default="default",
                max_length=40,
                verbose_name="density",
            ),
        ),
    ]
