# Generated by Django 4.1.7 on 2023-05-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('type', models.CharField(max_length=255, null=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organisations.orgnisation')),
            ],
            options={
                'db_table': 'Projects',
            },
        ),
    ]
