# Generated by Django 5.0.2 on 2024-02-09 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tilaus', '0004_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toimittaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tuotesarja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='toimittajan_tuotekoodi',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='toimittaja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tilaus.toimittaja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='tuotesarja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tilaus.tuotesarja'),
            preserve_default=False,
        ),
    ]
