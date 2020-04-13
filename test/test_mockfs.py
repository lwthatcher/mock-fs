"""Testing module for testing the mock file-system and its various components.

Tests here differ from `test_entities.py` in that valid path construction
is *required* for measuring expected behavior.
"""
import unittest
from unittest import TestCase
from mockfs import MockFileSystem
from mockfs.util import IllegalFSOpError, NotATextFileError


class TestMockFileSystem(TestCase):
  # region [Public Method Tests]
  def setUp(self):
    self.fs = MockFileSystem()

  def test_Create(self):
    # can create drives
    self.fs.Create('drive', 'X', None)
    self.assertEqual(len(self.fs.entities), 1)
    # can create folders
    self.fs.Create('folder', 'folder1', 'X')
    self.assertEqual(len(self.fs.entities), 2)
    # can create nested folders
    self.fs.Create('folder', 'folder2', 'X\\folder1')
    self.assertEqual(len(self.fs.entities), 3)
    # can create zip files (nested in folder)
    self.fs.Create('zip', 'zippy', 'X\\folder1')
    self.assertEqual(len(self.fs.entities), 4)
    # can create text files (nested in folder)
    self.fs.Create('text', 'file.txt', 'X\\folder1')
    self.assertEqual(len(self.fs.entities), 5)

  def test_Create__drive_constraints(self):
    # only drives can be top-level
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('folder', 'X', None)
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('zip', 'X', None)
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('text', 'X', None)
    # drives cannot be nested
    self.fs.Create('drive', 'Y', None)  # should succeed
    self.fs.Create('folder', 'f1', 'Y') # should also succeed
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('drive', 'Z', 'Y')  # should raise error
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('drive', 'Q', 'Y\\f1')  # should raise error

  def test_Create__drive__falsy_path(self):
    # path is empty string
    self.fs.Create('drive', 'X', '')
    self.assertEqual(len(self.fs.entities), 1)
    # path is empty list
    self.fs.Create('drive', 'Y', [])
    self.assertEqual(len(self.fs.entities), 2)
    # path is empty tuple
    self.fs.Create('drive', 'Z', ())
    self.assertEqual(len(self.fs.entities), 3)
    # Note: don't do these last two, but they're technically valid

  def test_Create__text_file_nesting(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('text', 'T', 'X')
    # cannot nest folders inside of text files
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('folder', 'f1', 'X\\T')
    # cannot nest zips inside of text files
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('zip', 'Z', 'X\\T')
    # cannot nest other text files inside of text files
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('text', 'text.txt', 'X\\T')

  def test_Create__invalid_type(self):
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Create('foo', 'bar', None)
    self.assertEqual(str(cm.exception), 'Unsupported type: "foo"')

  def test_Create__duplicate_entities(self):
    self.fs.Create('drive', 'X', None)  # should succeed
    with self.assertRaises(FileExistsError) as cm:
      self.fs.Create('drive', 'X', None)  # should not succeed

  def test_Create__missing_parents(self):
    # missing single parent (drive)
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Create('folder', 'X', 'dir')
    # missing single parent (folder)
    self.fs.Create('drive', 'Y', None)  # should succeed
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Create('folder', 'Y\\folder1', 'folder2')
    # missing multiple parents
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Create('folder', 'X\\folder1\\folder2', 'dir')
    
  def test_Delete(self):
    # can delete drives
    self.fs.Create('drive', 'X', None)
    self.assertEqual(len(self.fs.entities), 1)
    self.fs.Delete('X')
    self.assertEqual(len(self.fs.entities), 0)
    # can delete folders
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('folder', 'badfolder', 'Y')
    self.assertEqual(len(self.fs.entities), 2)
    self.fs.Delete('Y\\badfolder')
    self.assertEqual(len(self.fs.entities), 1)
    
  def test_Delete__recursive(self):
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('folder', 'f1', 'Y')
    self.fs.Create('folder', 'f2', 'Y\\f1')
    self.assertEqual(len(self.fs.entities), 2)
    self.fs.Delete('Y')
    self.assertEqual(len(self.fs.entities), 0)

  def test_Delete__does_not_exist(self):
    # empty file-system
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Delete('Q')
    # wrong target
    self.fs.Create('drive', 'X', None)
    self.assertEqual(len(self.fs.entities), 1)
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Delete('Y')
    self.assertEqual(len(self.fs.entities), 1)
    # not idempotent
    self.fs.Delete('X') # should succeed
    self.assertEqual(len(self.fs.entities), 0)
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Delete('X')  # should raise an error
    self.assertEqual(len(self.fs.entities), 0)

  @unittest.expectedFailure
  def test_Move(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('text', 'text.txt', 'X')
    # text file is in drive X
    self.assertTrue(self.fs.exists(('X', 'text.txt')))
    self.assertFalse(self.fs.exists(('Y', 'text.txt')))
    self.assertEqual(len(self.fs.entities), 3)
    # text file is in drive Y after move
    self.fs.Move('X\\text.txt', 'Y\\text.txt')
    self.assertFalse(self.fs.exists(('X', 'text.txt')))
    self.assertTrue(self.fs.exists(('Y', 'text.txt')))
    self.assertEqual(len(self.fs.entities), 3)  # file-system size unchanged

  @unittest.expectedFailure
  def test_Move__recursive(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('folder', 'F', 'X')
    self.fs.Create('zip', 'Z', 'X\\F')
    self.fs.Create('text', 'text.txt', 'X\\F\\Z')
    # text file is nested in drive X
    self.assertTrue(self.fs.exists(('X', 'F', 'Z', 'text.txt')))
    self.assertFalse(self.fs.exists(('Y', 'F', 'Z', 'text.txt')))
    self.assertEqual(len(self.fs.entities), 5)
    # text file is nested in drive Y after move
    self.fs.Move('X\\F\\Z\\text.txt', 'X\\F\\Z\\text.txt')
    self.assertFalse(self.fs.exists(('X', 'F', 'Z', 'text.txt')))
    self.assertTrue(self.fs.exists(('Y', 'F', 'Z', 'text.txt')))
    self.assertEqual(len(self.fs.entities), 5)  # file-system size unchanged

  @unittest.expectedFailure
  def test_Move__src_does_not_exist(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('text', 'text.txt', 'X')
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Move('X\\foo.txt', 'Y\\foo.txt')

  @unittest.expectedFailure
  def test_Move__dest_already_exists(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('text', 'text.txt', 'Y')
    self.fs.Create('text', 'text.txt', 'X')
    with self.assertRaises(FileExistsError) as cm:
      self.fs.Move('X\\text.txt', 'Y\\text.txt')

  @unittest.expectedFailure
  def test_Move__dest_parent_does_not_exist(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('text', 'text.txt', 'X')
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.Move('X\\text.txt', 'Y\\text.txt')

  @unittest.expectedFailure
  def test_Move__drive_constraints(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('text', 'text.txt', 'X')
    with self.assertRaises(IllegalFSOpError) as cm:
      self.fs.Move('X\\text.txt', 'text.txt')
    
  def test_WriteToFile(self):
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('text', 'textfile', 'Y')
    # initially empty
    t = self.fs.get(('Y', 'textfile'))
    self.assertEqual(t.Content, "")
    self.assertEqual(len(self.fs.entities), 2)
    # writes content correctly
    self.fs.WriteToFile('Y\\textfile', 'Hello World')
    t = self.fs.get(('Y', 'textfile'))
    self.assertEqual(t.Content, 'Hello World')
    self.assertEqual(len(self.fs.entities), 2)  # file-system remains same size
    # overwrites text upon additional calls
    self.fs.WriteToFile('Y\\textfile', 'foo bar')
    t = self.fs.get(('Y', 'textfile'))
    self.assertEqual(t.Content, 'foo bar')
    self.assertEqual(len(self.fs.entities), 2)  # file-system size still unchanged

  def test_WriteToFile__invalid_path(self):
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('text', 'textfile', 'Y')
    # incorrect file-name
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.WriteToFile('Y\\foofile', 'Hello')
    # wrong drive
    with self.assertRaises(FileNotFoundError) as cm:
      self.fs.WriteToFile('X\\textfile', 'Hello')

  def test_WriteToFile__not_a_text_file(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('folder', 'Y', 'X')
    self.fs.Create('zip', 'Z.txt', 'X\\Y')
    # cannot write to zip files
    with self.assertRaises(NotATextFileError) as cm:
      self.fs.WriteToFile('X\\Y\\Z.txt', 'Foo')
    # cannot write to folders
    with self.assertRaises(NotATextFileError) as cm:
      self.fs.WriteToFile('X\\Y', 'Foo')
    # cannot write to drives
    with self.assertRaises(NotATextFileError) as cm:
      self.fs.WriteToFile('X', 'Foo')
  # endregion

  # region [Implementation Tests]
  def test_constructor(self):
    fs = MockFileSystem()
    # by default there are no items initially in the file-system
    self.assertEqual(len(fs.entities), 0)

  def test_get(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('folder', 'Y', 'X')
    self.fs.Create('zip', 'Z', 'X\\Y')
    x = self.fs.get(('X',))
    y = self.fs.get(('X', 'Y'))
    z = self.fs.get(('X', 'Y', 'Z'))
    self.assertEqual(x.Type, 'drive')
    self.assertEqual(y.Type, 'folder')
    self.assertEqual(z.Type, 'zip')

  def test_parents_exist(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('folder', 'Y', 'X')
    self.assertTrue(self.fs.parents_exist(('X', 'Y', 'Z')))
    self.assertTrue(self.fs.parents_exist(('X', 'foo')))
    self.assertTrue(self.fs.parents_exist(('X', 'Y')))
    self.assertFalse(self.fs.parents_exist(('X', 'Y', 'Z', 'ducks')))
    self.assertFalse(self.fs.parents_exist(('X', 'Z', 'ducks')))

  def test_exists(self):
    self.fs.Create('drive', 'X', None)
    self.fs.Create('folder', 'Y', 'X')
    self.assertTrue(self.fs.exists(('X', 'Y')))
    self.assertTrue(self.fs.exists(('X',)))
    self.assertFalse(self.fs.exists(('Y', 'X')))
    self.assertFalse(self.fs.exists(('foobar',)))

  def test_get_children(self):
    self.fs.Create('drive', 'A', None)
    self.fs.Create('folder', 'B', 'A')
    self.fs.Create('folder', 'C', 'A\\B')
    self.fs.Create('zip', 'D1', 'A\\B\\C')
    self.fs.Create('text', 'D2', 'A\\B\\C')
    self.fs.Create('folder', 'R', 'A')
    self.fs.Create('drive', 'X', None)
    # children of A\B
    children = self.fs.get_children(('A', 'B'))
    self.assertEqual(len(children), 1)
    self.assertSetEqual({c.Name for c in children}, {'C',})
    # children of A\B\C
    children = self.fs.get_children(('A', 'B', 'C'))
    self.assertEqual(len(children), 2)
    self.assertSetEqual({c.Name for c in children}, {'D1', 'D2'})
  # endregion
