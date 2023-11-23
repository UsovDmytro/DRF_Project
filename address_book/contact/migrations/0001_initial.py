# Generated by Django 4.2.4 on 2023-11-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('url', models.URLField(unique=True)),
                ('phone', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='contacts/')),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
