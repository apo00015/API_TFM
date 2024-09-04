import unittest
from services.service_tfm import ServiceTFM
from routes.router import router
class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        # Configurar la app para las pruebas
        self.service = ServiceTFM()

    def test_get_items(self):
        response, status = self.service.getDocuments(1)
        self.assertEqual(status, 200)
    
    def test_get_items_404(self):
        response, status = self.service.getDocuments(10)
        self.assertEqual(status, 404)

    def test_get_items_500(self):
        self.service.db = None
        response, status = self.service.getDocuments(1)
        self.assertEqual(status, 500)

if __name__ == '__main__':
    unittest.main()

