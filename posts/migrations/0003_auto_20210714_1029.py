# Generated by Django 3.2.5 on 2021-07-14 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0002_remove_post_escription'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='post_imag'),
        ),
    ]
