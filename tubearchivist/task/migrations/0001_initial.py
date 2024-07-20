# Generated by Django 5.0.7 on 2024-07-20 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("django_celery_beat", "0018_improve_crontab_helptext"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomPeriodicTask",
            fields=[
                (
                    "periodictask_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_celery_beat.periodictask",
                    ),
                ),
                ("task_config", models.JSONField(default=dict)),
            ],
            bases=("django_celery_beat.periodictask",),
        ),
    ]
