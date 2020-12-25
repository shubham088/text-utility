# Generated by Django 2.2 on 2020-12-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCollections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('animal', 'Animal'), ('scenary', 'Scenary'), ('cars', 'Cars'), ('bike', 'Bikes')], max_length=255)),
                ('img', models.ImageField(upload_to='images')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
