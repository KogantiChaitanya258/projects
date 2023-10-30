# Generated by Django 3.0.5 on 2021-05-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210502_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='donorregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField(max_length=40)),
                ('gender', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('bloodgroup', models.CharField(max_length=3)),
                ('date', models.DateField(max_length=40)),
                ('ill', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
