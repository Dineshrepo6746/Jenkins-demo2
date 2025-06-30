import unittest
from app import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, Jenkins!")
    def test_fail(self):
        self.fail("Intentional failure to demonstrate Jenkins build failure.")

if __name__ == "__main__":
    unittest.main()
