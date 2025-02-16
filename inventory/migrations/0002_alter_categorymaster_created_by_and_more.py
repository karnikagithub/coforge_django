# Generated by Django 5.0.3 on 2024-03-19 08:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymaster',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inventorystockmaster',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itemmaster',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='locationmaster',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='location_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
