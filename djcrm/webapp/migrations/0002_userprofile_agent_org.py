# Generated by Django 5.0.2 on 2024-02-12 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='org',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='webapp.userprofile'),
            preserve_default=False,
        ),
    ]
