# Generated by Django 3.1.2 on 2020-11-25 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('mrp', models.FloatField()),
                ('discount', models.FloatField()),
                ('price', models.FloatField()),
                ('quantity', models.FloatField(blank=True)),
                ('origin', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('sold_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('stars', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
                ('reviewby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
