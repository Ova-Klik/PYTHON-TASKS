from unittest import TestCase
from stringmodifier_ingfunction import string_modifier_add_ing

class TestClass(TestCase):
    def test_for_entry_same_when_length_is_less_than_three(entry, get_string_test):
        entry_modifier=string_modifier_add_ing()
