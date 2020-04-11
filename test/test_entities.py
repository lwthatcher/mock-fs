from unittest import TestCase
from mockfs import MockFileSystem
from mockfs.entities import FolderEntity, DriveEntity, TextFileEntity, ZipFileEntity

class TestFolderEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = FolderEntity(fs, ('D', 'dir'))
    self.assertIsInstance(f, FolderEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = FolderEntity(fs, ('D', 'dir'))
    self.assertEqual(f.Type, 'folder')


class TestDriveEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = DriveEntity(fs, ('D'))
    self.assertIsInstance(f, DriveEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = DriveEntity(fs, ('D'))
    self.assertEqual(f.Type, 'drive')


class TestTextFileEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, ('D', 'file.txt'))
    self.assertIsInstance(f, TextFileEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, ('D', 'file.txt'))
    self.assertEqual(f.Type, 'text')


class TestZipFileEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = ZipFileEntity(fs, ('D', 'zippy.zip'))
    self.assertIsInstance(f, ZipFileEntity)

  def test_Type(self):
    fs = MockFileSystem()
    f = ZipFileEntity(fs, ('D', 'zippy.zip'))
    self.assertEqual(f.Type, 'zip')
