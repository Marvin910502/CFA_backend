# Generated by Django 4.2 on 2023-09-07 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='parking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equations.parking'),
        ),
    ]
