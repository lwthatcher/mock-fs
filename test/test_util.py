from unittest import TestCase
from mockfs.util import split_path


class TestUtil(TestCase):

  def test_split_path(self):
    # single-item string
    path = split_path('D')
    self.assertEqual(path, ('D',))
    # multi-item string
    path = split_path('D\\dir\\subdir\\zip')
    self.assertEqual(path, ('D', 'dir', 'subdir', 'zip'))
    # tuple
    path = split_path(('D', 'dir', 'subdir', 'zip'))
    self.assertEqual(path, ('D', 'dir', 'subdir', 'zip'))
    # list
    path = split_path(['D', 'dir', 'subdir', 'zip'])
    self.assertEqual(path, ('D', 'dir', 'subdir', 'zip'))
