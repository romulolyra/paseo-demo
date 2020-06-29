# Generated by Django 3.0.7 on 2020-06-27 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NovoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('senha1', models.CharField(max_length=50)),
                ('senha2', models.CharField(max_length=50)),
                ('largadouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=10)),
                ('curso', models.CharField(choices=[('cc', 'Ciências da computação'), ('ds', 'Design')], max_length=25)),
                ('placa', models.CharField(max_length=9)),
                ('cor', models.CharField(max_length=19)),
                ('modelo', models.CharField(max_length=19)),
                ('reserva1', models.CharField(max_length=50)),
                ('reserva2', models.CharField(max_length=50)),
                ('e1', models.BooleanField(default=False)),
                ('e2', models.BooleanField(default=False)),
                ('e3', models.BooleanField(default=False)),
                ('e4', models.BooleanField(default=False)),
                ('r1', models.BooleanField(default=False)),
                ('r2', models.BooleanField(default=False)),
                ('r3', models.BooleanField(default=False)),
                ('r4', models.BooleanField(default=False)),
                ('j1', models.BooleanField(default=False)),
                ('j2', models.BooleanField(default=False)),
                ('j3', models.BooleanField(default=False)),
                ('j4', models.BooleanField(default=False)),
                ('j5', models.BooleanField(default=False)),
                ('j6', models.BooleanField(default=False)),
                ('a1', models.BooleanField(default=False)),
                ('a2', models.BooleanField(default=False)),
                ('a3', models.BooleanField(default=False)),
                ('a4', models.BooleanField(default=False)),
                ('a5', models.BooleanField(default=False)),
                ('a6', models.BooleanField(default=False)),
                ('s1', models.BooleanField(default=False)),
                ('s2', models.BooleanField(default=False)),
                ('s3', models.BooleanField(default=False)),
                ('s4', models.BooleanField(default=False)),
                ('h1', models.BooleanField(default=False)),
                ('h2', models.BooleanField(default=False)),
                ('h3', models.BooleanField(default=False)),
                ('h4', models.BooleanField(default=False)),
                ('h5', models.BooleanField(default=False)),
                ('h6', models.BooleanField(default=False)),
                ('so1', models.BooleanField(default=False)),
                ('so2', models.BooleanField(default=False)),
                ('so3', models.BooleanField(default=False)),
                ('so4', models.BooleanField(default=False)),
                ('v1', models.BooleanField(default=False)),
                ('v2', models.BooleanField(default=False)),
                ('v3', models.BooleanField(default=False)),
                ('v4', models.BooleanField(default=False)),
                ('v5', models.BooleanField(default=False)),
                ('v6', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='placa',
        ),
    ]