# Generated by Django 4.1.7 on 2023-02-22 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.component')),
            ],
        ),
    ]
