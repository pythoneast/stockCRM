# Generated by Django 2.1.3 on 2018-11-30 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ST', 'In stock'), ('WA', 'Waiting for receipt'), ('NA', 'Not available')], default='NA', max_length=2)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]