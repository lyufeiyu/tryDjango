# Generated by Django 4.2.8 on 2024-01-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_active_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True),
        ),
    ]