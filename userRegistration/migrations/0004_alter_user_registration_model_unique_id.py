# Generated by Django 5.0.4 on 2024-04-07 10:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0003_alter_user_registration_model_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration_model',
            name='unique_id',
            field=models.CharField(default=uuid.uuid4, max_length=10, unique=True),
        ),
    ]