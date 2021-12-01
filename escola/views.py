from rest_framework import serializers, viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunosSerializer, CursosSerializer

# com essa linha de código será possível manipular todas as requisições que queremos diponibilizar

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer



