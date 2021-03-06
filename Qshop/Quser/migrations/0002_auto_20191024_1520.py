# Generated by Django 2.2.6 on 2019-10-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
                ('username', models.CharField(blank=True, default=models.EmailField(blank=True, max_length=254, null=True), max_length=32, null=True)),
                ('gender', models.CharField(blank=True, max_length=8, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(default='/image/0.jpg', upload_to='image')),
            ],
        ),
        migrations.DeleteModel(
            name='Quser',
        ),
    ]
