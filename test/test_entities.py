from unittest import TestCase
from mockfs import MockFileSystem
from mockfs.entities import FolderEntity, DriveEntity, TextFileEntity, ZipFileEntity

class TestFolderEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = FolderEntity(fs, ('D', 'folder'))
    self.assertIsInstance(f, FolderEntity)


class TestDriveEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = DriveEntity(fs, ('D'))
    self.assertIsInstance(f, DriveEntity)


class TestTextFileEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = TextFileEntity(fs, ('D', 'file.txt'))
    self.assertIsInstance(f, TextFileEntity)


class TestZipFileEntity(TestCase):

  def test_constructor(self):
    fs = MockFileSystem()
    f = ZipFileEntity(fs, ('D', 'folder'))
    self.assertIsInstance(f, ZipFileEntity)
