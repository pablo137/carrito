# Generated by Django 3.0.6 on 2023-05-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='uploads/products/img_defecto.jpg', upload_to='uploads/products/'),
        ),
    ]