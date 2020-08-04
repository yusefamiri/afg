# Generated by Django 2.2.7 on 2019-11-29 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('token', models.CharField(max_length=5, unique=True)),
                ('symbol', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='short_description',
            field=models.TextField(max_length=150),
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change', models.DecimalField(decimal_places=2, max_digits=6)),
                ('change_date', models.DateField(auto_now_add=True)),
                ('change_time', models.TimeField(auto_now_add=True)),
                ('currency', models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='currency', to='blog.Currency' )),
            ],
        ),
    ]
