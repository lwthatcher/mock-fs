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

  def test_split_path__name_included(self):
    # single-item string + name
    path = split_path('D', 'dir')
    self.assertEqual(path, ('D', 'dir'))
    # multi-item string + name
    path = split_path('D\\dir\\subdir\\zip', 'file.txt')
    self.assertEqual(path, ('D', 'dir', 'subdir', 'zip', 'file.txt'))
    # tuple + name
    path = split_path(('D', 'dir', 'subdir', 'zip'), 'file.txt')
    self.assertEqual(path, ('D', 'dir', 'subdir', 'zip', 'file.txt'))
    # list + name
    path = split_path(['D', 'dir', 'subdir', 'zip'], 'file.txt')
    self.assertEqual(path, ('D', 'dir', 'subdir', 'zip', 'file.txt'))

  def test_split_path__empty_path__name_included(self):
    path = split_path('', 'name')
    self.assertEqual(path, ('name',))

  def test_split_path__null_path__name_included(self):
    path = split_path(None, 'name')
    self.assertEqual(path, ('name',))

  def test_split_path__empty_name(self):
    # probably not desirable, but currently the expected behavior
    path = split_path('D', '')
    self.assertEqual(path, ('D', ''))

