# Generated by Django 4.0 on 2023-02-10 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_alter_test_hashtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settest',
            old_name='category',
            new_name='test',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='title',
            new_name='description',
        ),
    ]