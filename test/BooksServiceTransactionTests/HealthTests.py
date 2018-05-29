import unittest
from BooksServiceTransaction.Controllers import HealthController

class HealthTests(unittest.TestCase):
    
    def setUp(self):
        self.dut = HealthController()

    def testhealth_whenok_then200(self):
        (resultStr, resultInt) = self.dut.Ok()
        self.assertEqual(resultInt, 200)
    