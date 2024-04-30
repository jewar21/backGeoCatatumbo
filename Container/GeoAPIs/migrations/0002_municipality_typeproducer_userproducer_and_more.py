# Generated by Django 4.1.13 on 2024-04-30 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeoAPIs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('ABREGO', 'Abrego'), ('OCANA', 'Ocaña'), ('EL CARMEN', 'El Carmen'), ('CONVENCION', 'Convención'), ('TEORAMA', 'Teorama'), ('SAN CALIXTO', 'San Calixto'), ('HACARI', 'Hacarí'), ('LA PLAYA DE BELEN', 'La Playa de Belén'), ('EL TARRA', 'El Tarra'), ('TIBU', 'Tibú'), ('SARDINATA', 'Sardinata')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeProducer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProducer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('dependency', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_producers', to='GeoAPIs.municipality')),
                ('type_producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_producers', to='GeoAPIs.typeproducer')),
            ],
        ),
        migrations.RemoveField(
            model_name='userproducers',
            name='type_producer',
        ),
        migrations.DeleteModel(
            name='TypeProducers',
        ),
        migrations.DeleteModel(
            name='UserProducers',
        ),
    ]
