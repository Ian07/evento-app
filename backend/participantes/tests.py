from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from participantes.models import Persona
from participantes.serializers import PersonaSerializer

class BaseViewTest(APITestCase):
    cliente = APIClient()

    @staticmethod
    def crear_persona(documento, nombre, apellido):
        Persona.objects.create(documento=documento, nombre=nombre, apellido=apellido)

    def setUp(self):
        self.crear_persona(38804362, "Matías", "Acosta")
        self.crear_persona(38800940, "Ian", "Mazzaglia")
        self.crear_persona(20200200, "Diego", "Martinez")

class PersonasTest(BaseViewTest):

    def test_get_all_personas(self):
        """
        Teste para probar /personas
        """
        response = self.client.get(
            reverse("personas-all", kwargs={"version":"v1"})
        )

        expected = Persona.objects.all()
        serialized = PersonaSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)