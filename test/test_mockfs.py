from unittest import TestCase
from mockfs import MockFileSystem
from mockfs.util import IllegalFileSystemOperationError


class TestMockFileSystem(TestCase):

  # region [Public Method Tests]
  def test_Create(self):
    fs = MockFileSystem()
    # can create drives
    fs.Create('drive', 'X', None)
    self.assertEqual(len(fs.entities), 1)

  def test_Create__requires_valid_type(self):
    fs = MockFileSystem()
    with self.assertRaises(IllegalFileSystemOperationError) as cm:
      fs.Create('foo', 'bar', None)
    self.assertEqual(str(cm.exception), 'Unsupported type: "foo"')

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
      self.assertEqual(len(fs.entities), 0)
  # endregion
