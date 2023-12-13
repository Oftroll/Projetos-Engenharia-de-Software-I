from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField()
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}{self.pai}{self.mae}{self.cpf}{self.data_nascimento}{self.email}{self.cidade}'

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}{self.telefone}{self.cidade}'

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}{self.carga_horaria_total}{self.duracao_meses}{self.area_saber}{self.instituicao_ensino}'

class PeriodoCurso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}{self.area_saber}'

class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f'{self.instituicao_ensino}{self.curso}{self.pessoa}{self.data_inicio}{self.data_previsao_termino}'

class Avaliacoes(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}{self.curso}{self.disciplina}'

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f'{self.curso}{self.disciplina}{self.numero_faltas}'

class Turmas(models.Model):
    nome = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}{self.periodo}'
  
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome}{self.uf}'

class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao}{self.data}{self.curso}{self.disciplina}{self.pessoa}'

class DisciplinasPorCursos(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoCurso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}{self.carga_horaria}{self.curso}{self.periodo}'

class TipoAvalicao(models.Model):
    nome = models.CharField(max_length=100)
    