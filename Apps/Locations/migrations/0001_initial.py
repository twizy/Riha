# Generated by Django 2.2.5 on 2020-04-20 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('fullname_area_chief', models.CharField(default='Area chief', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('fullname_city_chief', models.CharField(default='City chief', max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Locations.Area')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('fullname_district_chief', models.CharField(default='District chief', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50)),
                ('fullname_province_chief', models.CharField(default='Province chief', max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Locations.City')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Locations.District'),
        ),
    ]