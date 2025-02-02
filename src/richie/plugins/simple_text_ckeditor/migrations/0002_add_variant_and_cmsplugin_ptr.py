# Generated by Django 4.2.16 on 2024-11-13 00:09

import django.db.models.deletion
from django.db import migrations, models

from ..defaults import SIMPLETEXT_VARIANTS


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("simple_text_ckeditor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="simpletext",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=SIMPLETEXT_VARIANTS,
                default="",
                help_text="Enable a themed box to enclose content.",
                max_length=50,
                verbose_name="Box variant",
            ),
        ),
        migrations.AlterField(
            model_name="simpletext",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
    ]
