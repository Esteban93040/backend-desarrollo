from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models import Obra, informes, Avances, asignarTareas
from datetime import date

class ObraModelTest(TestCase):
    def test_create_obra(self):
        # Crear una instancia de Obra y verificar los campos
        obra = Obra.objects.create(
            idObra=1,
            idDirector=101,
            idCapataz=201,
            idAyudante=301,
            idPeon=401,
            nombreObra="Construcción A",
            estadoObra="Activa",
            fechaInicioObra=date(2024, 1, 1)
        )
        self.assertEqual(obra.idObra, 1)
        self.assertEqual(obra.idDirector, 101)
        self.assertEqual(obra.nombreObra, "Construcción A")
        self.assertEqual(obra.estadoObra, "Activa")
        self.assertEqual(obra.fechaInicioObra, date(2024, 1, 1))