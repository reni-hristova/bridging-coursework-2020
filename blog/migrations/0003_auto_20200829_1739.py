# Generated by Django 2.2.13 on 2020-08-29 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
