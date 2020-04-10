from unittest import TestCase
from mockfs import MockFileSystem

class TestMockFileSystem(TestCase):
  
  def test_constructable(self):
    fs = MockFileSystem()

  # region [Public Method Tests]
  def test_Create(self):
    fs = MockFileSystem()
    self.assertEqual(fs.entities, [])
    fs.Create('drive', 'X', None)
    self.assertEqual(len(fs.entities), 1)

  def test_Delete(self):
    pass

  def test_Move(self):
    pass

  def test_WriteToFile(self):
    pass
  # endregion

