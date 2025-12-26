from unittest import TestCase
from stringmodifier_ingfunction import string_modifier_add_ing

class TestClass(TestCase):
    def test_that_entry_is_same_when_length_is_less_than_three(self):
        result=string_modifier_add_ing("se", "seing")
        self.assertTrue(result)
