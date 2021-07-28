# Generated by Django 3.2.5 on 2021-07-28 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('valor_diaria', models.FloatField()),
                ('foto', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaHospedagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.FloatField()),
                ('data_reserva', models.DateField()),
                ('hospedagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospedagem.hospedagem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hospedagem',
            name='locatario',
            field=models.ManyToManyField(through='hospedagem.ReservaHospedagem', to=settings.AUTH_USER_MODEL),
        ),
    ]