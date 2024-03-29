# Generated by Django 3.2.24 on 2024-02-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0005_visitorlog_status_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitor",
            name="max_uses",
            field=models.PositiveSmallIntegerField(
                default=5, help_text="Maximum allowed uses of the token."
            ),
        ),
        migrations.AddField(
            model_name="visitor",
            name="uses",
            field=models.PositiveSmallIntegerField(default=0, editable=False),
        ),
    ]
