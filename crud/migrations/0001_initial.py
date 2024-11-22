# Generated by Django 5.1.3 on 2024-11-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('año', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_combustible', models.CharField(choices=[('Gasolina', 'Gasolina'), ('Diesel', 'Diesel'), ('Eléctrico', 'Eléctrico')], max_length=20)),
                ('kilometraje', models.PositiveIntegerField()),
            ],
        ),
    ]
