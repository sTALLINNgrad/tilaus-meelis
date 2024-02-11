# Generated by Django 5.0.2 on 2024-02-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tilaus', '0003_product_kuva_alter_product_s_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]