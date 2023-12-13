from django.db import models


class SerieEpisodios(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.IntegerField()
    data_disponibilizacao = models.DateField()

    def __str__(self):
        return self.nome


class Temporada(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Continente(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Pais(models.Model):
    nome = models.CharField(max_length=255)
    continente = models.ForeignKey('Continente', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class AtorDiretor(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()
    insta = models.URLField()
    face = models.URLField()
    twitter = models.URLField()
    nacionalidade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Serie(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.IntegerField()
    sinopse = models.TextField()
    site_oficial = models.URLField()
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(AtorDiretor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.IntegerField()
    sinopse = models.TextField()
    site_oficial = models.URLField()
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(AtorDiretor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class SeriesComEpisodios(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    episodio = models.ForeignKey(SerieEpisodios, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serie} - {self.episodio}'


class FilmesAtores(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ForeignKey(AtorDiretor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.filme} - {self.ator}'
