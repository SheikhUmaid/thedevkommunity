# Generated by Django 2.0.7 on 2022-05-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('content', models.TextField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
