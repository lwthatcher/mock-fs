from unittest import TestCase
from mockfs import MockFileSystem
from mockfs.util import IllegalFileSystemOperationError


class TestMockFileSystem(TestCase):
  # region [Public Method Tests]
  def setUp(self):
    self.fs = MockFileSystem()

  def test_Create(self):
    # can create drives
    self.fs.Create('drive', 'X', None)
    self.assertEqual(len(self.fs.entities), 1)
    # can create folders
    self.fs.Create('folder', 'X', 'folder1')
    self.assertEqual(len(self.fs.entities), 2)
    # can create nested folders
    self.fs.Create('folder', 'X\\folder1', 'folder2')
    self.assertEqual(len(self.fs.entities), 3)
    # can create zip files (nested in folder)
    self.fs.Create('zip', 'X\\folder1', 'zippy')
    self.assertEqual(len(self.fs.entities), 4)
    # can create text files (nested in folder)
    self.fs.Create('text', 'X\\folder1', 'file.txt')
    self.assertEqual(len(self.fs.entities), 5)

  def test_Create__drive_constrains(self):
    # only drives can be top-level
    with self.assertRaises(IllegalFileSystemOperationError) as cm:
      self.fs.Create('folder', 'X', None)
    with self.assertRaises(IllegalFileSystemOperationError) as cm:
      self.fs.Create('zip', 'X', None)
    with self.assertRaises(IllegalFileSystemOperationError) as cm:
      self.fs.Create('text', 'X', None)
    # drives cannot be nested
    self.fs.Create('drive', 'Y', None)  # should succeed
    self.fs.Create('folder', 'f1', 'Y') # should also succeed
    with self.assertRaises(IllegalFileSystemOperationError) as cm:
      self.fs.Create('drive', 'Z', 'Y')  # should raise error
    with self.assertRaises(IllegalFileSystemOperationError) as cm:
      self.fs.Create('drive', 'Q', 'Y\\f1')  # should raise error

  def test_Create__invalid_type(self):
    with self.assertRaises(IllegalFileSystemOperationError) as cm:
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

  def test_Move(self):
    pass

  def test_WriteToFile(self):
    pass
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
  # endregion
