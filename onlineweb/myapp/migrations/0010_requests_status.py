# Generated by Django 3.0.5 on 2021-06-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210531_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=10, null=True),
        ),
    ]
