# Generated by Django 5.1.1 on 2024-09-25 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_note_ethnicity_note_lunch_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="content",
        ),
    ]
