# Generated by Django 3.2 on 2021-06-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('avail_bal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transectiondetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('deb_amt', models.IntegerField()),
                ('cr_amt', models.IntegerField()),
                ('ac_bal', models.IntegerField()),
            ],
        ),
    ]
