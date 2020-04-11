from unittest import TestCase
from mockfs import MockFileSystem
from mockfs.entities import FolderEntity, DriveEntity, TextFileEntity, ZipFileEntity

# region [Folder Tests]
class TestFolderEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = FolderEntity(fs, ('D', 'dir'))
    self.assertIsInstance(f, FolderEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = FolderEntity(fs, ('D', 'dir'))
    self.assertEqual(f.Type, 'folder')

  def test_Name(self):
    fs = MockFileSystem()
    f = FolderEntity(fs, ('D', 'dir'))
    self.assertEqual(f.Name, 'dir')
  
  def test_Path(self):
    fs = MockFileSystem()
    f = FolderEntity(fs, ('D', 'dir'))
    self.assertEqual(f.Path, 'D\\dir')
# endregion

# region [Drive Tests]
class TestDriveEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = DriveEntity(fs, ('D'))
    self.assertIsInstance(f, DriveEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = DriveEntity(fs, ('D'))
    self.assertEqual(f.Type, 'drive')

  def test_Name(self):
    fs = MockFileSystem()
    f = DriveEntity(fs, ('D'))
    self.assertEqual(f.Name, 'D')

  def test_Path(self):
    fs = MockFileSystem()
    f = DriveEntity(fs, ('D'))
    self.assertEqual(f.Path, 'D')
# endregion


# region [Text File Tests]
class TestTextFileEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, ('D', 'file.txt'))
    self.assertIsInstance(f, TextFileEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, ('D', 'file.txt'))
    self.assertEqual(f.Type, 'text')
  
  def test_Name(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, ('D', 'file.txt'))
    self.assertEqual(f.Name, 'file.txt')

  def test_Path(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, ('D', 'file.txt'))
    self.assertEqual(f.Path, 'D\\file.txt')
# endregion


# region [Zip File Tests]
class TestZipFileEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = ZipFileEntity(fs, ('D', 'zippy.zip'))
    self.assertIsInstance(f, ZipFileEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = ZipFileEntity(fs, ('D', 'zippy.zip'))
    self.assertEqual(f.Type, 'zip')

  def test_Name(self):
    fs = MockFileSystem()
    f = ZipFileEntity(fs, ('D', 'zippy.zip'))
    self.assertEqual(f.Name, 'zippy.zip')

  def test_Path(self):
    fs = MockFileSystem()
    f = ZipFileEntity(fs, ('D', 'zippy.zip'))
    self.assertEqual(f.Path, 'D\\zippy.zip')
# endregion
