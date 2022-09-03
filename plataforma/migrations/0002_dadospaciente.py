# Generated by Django 4.1 on 2022-09-01 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('percentual_gordura', models.FloatField()),
                ('percentual_musculo', models.FloatField()),
                ('colesterol_hdl', models.FloatField()),
                ('colesterol_ldl', models.FloatField()),
                ('colesterol_total', models.FloatField()),
                ('trigliceridios', models.FloatField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.pacientes')),
            ],
        ),
    ]
