from unittest import TestCase
from mockfs import MockFileSystem

class TestMockFileSystem(TestCase):

  # region [Public Method Tests]
  def test_Create(self):
    fs = MockFileSystem()
    # can create drives
    fs.Create('drive', 'X', None)
    self.assertEqual(len(fs.entities), 1)

  def test_Delete(self):
    pass

  def test_Move(self):
    pass

  def test_WriteToFile(self):
    pass
  # endregion

  # region [Implementation Tests]
  def test_constructor(self):
      fs = MockFileSystem()
      # by default there are no items initially in the file-system
      self.assertEqual(fs.entities, [])
  # endregion
