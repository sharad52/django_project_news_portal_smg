# Generated by Django 3.0.3 on 2020-04-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsport', '0003_auto_20200405_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('sports_type', models.CharField(choices=[('F', 'Football'), ('C', 'Cricket'), ('V', 'Volleyball'), ('H', 'Hockey')], max_length=50)),
            ],
        ),
    ]
