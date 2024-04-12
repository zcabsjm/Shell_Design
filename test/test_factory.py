import unittest
from Factory import Factory


class TestFactory(unittest.TestCase):
    def test_factory_safe_application(self):
        app = Factory("ls")
        self.assertFalse(app.is_unsafe())

    def test_factory_unsafe_application(self):
        app = Factory("_ls")
        self.assertTrue(app.is_unsafe())

    def test_factory_with_wrong_name_should_throw_exception(self):
        name = "zzz"
        self.assertRaises(ModuleNotFoundError, Factory, name)
