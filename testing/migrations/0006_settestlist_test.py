# Generated by Django 4.0 on 2023-02-11 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0005_alter_settest_test_alter_settestlist_set_test_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settestlist',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testing.test'),
        ),
    ]