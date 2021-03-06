# Generated by Django 2.2.13 on 2020-08-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200830_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='positionTitle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='entry',
            name='type',
            field=models.CharField(choices=[('education', 'Education'), ('experience', 'Experience'), ('achievement', 'Achievement')], default='experience', max_length=20),
        ),
    ]
