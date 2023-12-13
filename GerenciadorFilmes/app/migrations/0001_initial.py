# Generated by Django 4.2.5 on 2023-09-26 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtorDiretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('site', models.URLField()),
                ('insta', models.URLField()),
                ('face', models.URLField()),
                ('twitter', models.URLField()),
                ('nacionalidade', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('duracao', models.IntegerField()),
                ('sinopse', models.TextField()),
                ('site_oficial', models.URLField()),
                ('data_lancamento', models.DateField()),
                ('nota_avaliacao', models.DecimalField(decimal_places=1, max_digits=3)),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.atordiretor')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('continente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.continente')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('duracao', models.IntegerField()),
                ('sinopse', models.TextField()),
                ('site_oficial', models.URLField()),
                ('data_lancamento', models.DateField()),
                ('nota_avaliacao', models.DecimalField(decimal_places=1, max_digits=3)),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.atordiretor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='SerieEpisodios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('duracao', models.IntegerField()),
                ('data_disponibilizacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesComEpisodios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episodio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serieepisodios')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.temporada')),
            ],
        ),
        migrations.CreateModel(
            name='FilmesAtores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.atordiretor')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.filme')),
            ],
        ),
        migrations.AddField(
            model_name='filme',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero'),
        ),
        migrations.AddField(
            model_name='filme',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais'),
        ),
    ]