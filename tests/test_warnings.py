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


warnings.filterwarnings('error', category=PendingDeprecationWarning, message=".*0\.5\.0.*")


class TestWarnings(TestCase):

    def test_deprecation_warnings(self):
        with warnings.catch_warnings(record=True) as w:
            m = Machine()
            with self.assertRaises(PendingDeprecationWarning):
                m = Machine(None)
            with self.assertRaises(PendingDeprecationWarning):
                m = Machine(None, add_self=False)
            with self.assertRaises(PendingDeprecationWarning):
                m = Machine(None, initial=None)
