# Generated by Django 4.0.1 on 2022-06-25 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_address_fist_line_remove_address_pin_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='accounts.profile'),
        ),
    ]
