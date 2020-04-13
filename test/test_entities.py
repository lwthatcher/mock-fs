"""Testing module for directly testing methods on various entity objects.

Tests here differ from `test_mockfs.py` where the provided paths do
not necessarily have to be valid paths within the file-system.
"""
from unittest import TestCase
from mockfs import MockFileSystem
from mockfs.entities import entity
from mockfs.entities import Folder, Drive, TextFileEntity, ZipFile

# several constants used for convenience
FPATH = ('D', 'dir')
DPATH = ('D')
TPATH = ('D', 'file.txt')
ZPATH = ('D', 'zippy.zip')


# region [EntityFactoryTests]
class TestEntityFactory(TestCase):

  def setUp(self):
    self.fs = MockFileSystem()

  def test_entity__folder(self):
    f = entity(self.fs, 'folder', FPATH)
    self.assertIsInstance(f, Folder)

  def test_entity__drive(self):
    f = entity(self.fs, 'drive', DPATH)
    self.assertIsInstance(f, Drive)

  def test_entity__text_file(self):
    f = entity(self.fs, 'text', TPATH)
    self.assertIsInstance(f, TextFileEntity)

  def test_entity__zip_file(self):
    f = entity(self.fs, 'zip', ZPATH)
    self.assertIsInstance(f, ZipFile)

# endregion


# region [Folder Tests]
class TestFolder(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = Folder(fs, FPATH)
    self.assertIsInstance(f, Folder)

  def test_Type(self):
    fs = MockFileSystem()
    f = Folder(fs, FPATH)
    self.assertEqual(f.Type, 'folder')

  def test_Name(self):
    fs = MockFileSystem()
    f = Folder(fs, FPATH)
    self.assertEqual(f.Name, 'dir')
  
  def test_Path(self):
    fs = MockFileSystem()
    f = Folder(fs, FPATH)
    self.assertEqual(f.Path, 'D\\dir')
# endregion

# region [Drive Tests]
class TestDrive(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = Drive(fs, DPATH)
    self.assertIsInstance(f, Drive)

  def test_Type(self):
    fs = MockFileSystem()
    f = Drive(fs, DPATH)
    self.assertEqual(f.Type, 'drive')

  def test_Name(self):
    fs = MockFileSystem()
    f = Drive(fs, DPATH)
    self.assertEqual(f.Name, 'D')

  def test_Path(self):
    fs = MockFileSystem()
    f = Drive(fs, DPATH)
    self.assertEqual(f.Path, 'D')
# endregion


# region [Text File Tests]
class TestTextFileEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, TPATH)
    self.assertIsInstance(f, TextFileEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, TPATH)
    self.assertEqual(f.Type, 'text')
  
  def test_Name(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, TPATH)
    self.assertEqual(f.Name, 'file.txt')

  def test_Path(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, TPATH)
    self.assertEqual(f.Path, 'D\\file.txt')
# endregion


# region [Zip File Tests]
class TestZipFile(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = ZipFile(fs, ZPATH)
    self.assertIsInstance(f, ZipFile)

  def test_Type(self):
    fs = MockFileSystem()
    f = ZipFile(fs, ZPATH)
    self.assertEqual(f.Type, 'zip')

  def test_Name(self):
    fs = MockFileSystem()
    f = ZipFile(fs, ZPATH)
    self.assertEqual(f.Name, 'zippy.zip')

  def test_Path(self):
    fs = MockFileSystem()
    f = ZipFile(fs, ZPATH)
    self.assertEqual(f.Path, 'D\\zippy.zip')
# endregion
