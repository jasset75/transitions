try:
    from builtins import object
except ImportError:
    pass

import warnings
from transitions import Machine
from unittest import TestCase

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

warnings.simplefilter('always')


class TestWarnings(TestCase):

    def test_deprecation_warnings(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            m = Machine()
            self.assertEqual(len(w), 0)
            m = Machine(None)
            self.assertEqual(len(w), 1)
            self.assertEqual(w[-1].category, PendingDeprecationWarning)
            m = Machine(None, add_self=False)
            self.assertEqual(len(w), 2)
            self.assertEqual(w[-1].category, PendingDeprecationWarning)
            m = Machine(None, initial=None)
            self.assertEqual(len(w), 4)
            self.assertEqual(w[-1].category, PendingDeprecationWarning)
            self.assertEqual(m._initial, 'initial')
            self.assertTrue(m in m.models)
