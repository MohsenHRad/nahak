# Generated by Django 5.1.4 on 2025-01-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_active_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کد فعالسازی ایمیل'),
        ),
    ]
