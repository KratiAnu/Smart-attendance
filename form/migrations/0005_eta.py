# Generated by Django 3.0.1 on 2020-01-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('form', '0004_delete_deta'),
    ]

    operations = [
        migrations.CreateModel(
            name='eta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pis')),
                ('date', models.IntegerField()),
                ('month', models.CharField(max_length=100)),
                ('extra', models.TextField()),
                ('extra2', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
    ]