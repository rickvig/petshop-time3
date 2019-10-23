# Generated by Django 2.2.5 on 2019-10-23 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0010_auto_20191022_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServicoInterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario_inicial', models.DateTimeField()),
                ('data_horario_final', models.DateTimeField()),
                ('checkin', models.DateTimeField(blank=True, null=True)),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Agenda')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Animal')),
                ('produtos', models.ManyToManyField(to='core.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServicoExterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario_inicial', models.DateTimeField()),
                ('data_horario_final', models.DateTimeField()),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Agenda')),
                ('animals', models.ManyToManyField(to='core.Animal')),
            ],
        ),
    ]