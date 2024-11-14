# Generated by Django 3.2 on 2024-11-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0015_auto_20221215_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='extras',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='extras',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='extras',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='event',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='extras',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='extras',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]