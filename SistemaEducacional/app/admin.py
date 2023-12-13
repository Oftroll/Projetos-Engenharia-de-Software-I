from django.contrib import admin
from app.models import *

admin.site.register(Pessoa)
admin.site.register(Ocupacao)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(PeriodoCurso)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacoes)
admin.site.register(Frequencia)
admin.site.register(Turmas)
admin.site.register(Cidade)
admin.site.register(Ocorrencias)
admin.site.register(DisciplinasPorCursos)
admin.site.register(TipoAvalicao)

# Register your models here.
