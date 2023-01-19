# Generated by Django 4.1.5 on 2023-01-19 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField(default='No Description', max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.category')),
            ],
        ),
        migrations.DeleteModel(
            name='menu',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='BookingDate',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='No_of_guests',
        ),
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default='NA', max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]
