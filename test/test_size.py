"""module for testing the Size attribute of file-system entities"""
from unittest import TestCase
from mockfs import MockFileSystem


class TestSizeImplementation(TestCase):
  # region [Size Tests]
  def setUp(self):
    self.fs = MockFileSystem()
    self.fs.Create('drive', 'X', None)
    self.fs.Create('drive', 'Y', None)
    self.fs.Create('folder', 'A', 'X')
    self.fs.Create('folder', 'E', 'X')
    self.fs.Create('folder', 'B', 'X\\A')
    self.fs.Create('zip', 'Z', 'X\\A')
    self.fs.Create('zip', 'ZZ', 'X\\A\\Z')
    self.fs.Create('folder', 'C', 'X\\A\\B')
    self.fs.Create('folder', 'D', 'X\\A\\B')
    self.fs.Create('text', 'T0', 'X\\A\\B\\D')
    self.fs.Create('text', 'T1', 'X\\A\\B\\C')
    self.fs.Create('text', 'T2', 'X\\A\\B\\C')
    self.fs.Create('text', 'T3', 'X\\A\\Z')
    self.fs.Create('text', 'T4', 'X\\A\\Z\\ZZ')
    self.fs.get(('X', 'A', 'B', 'C', 'T1'))._content = '1234'
    self.fs.get(('X', 'A', 'B', 'C', 'T2'))._content = '123456'
    self.fs.get(('X', 'A', 'Z', 'T3'))._content = '123456'
    self.fs.get(('X', 'A', 'Z', 'ZZ', 'T4'))._content = '1234567890'

  def test_Size__text(self):
    # empty text file
    T0 = self.fs.get(('X', 'A', 'B', 'D', 'T0'))
    self.assertEqual(T0.Size, 0)
    # non-empty text files
    T1 = self.fs.get(('X', 'A', 'B', 'C', 'T1'))
    T2 = self.fs.get(('X', 'A', 'B', 'C', 'T2'))
    T3 = self.fs.get(('X', 'A', 'Z', 'T3'))
    T4 = self.fs.get(('X', 'A', 'Z', 'ZZ', 'T4'))
    self.assertEqual(T1.Size, 4)
    self.assertEqual(T2.Size, 6)
    self.assertEqual(T3.Size, 6)
    self.assertEqual(T4.Size, 10)

  def test_Size__text__value_changed(self):
    T0 = self.fs.get(('X', 'A', 'B', 'D', 'T0'))
    self.assertEqual(T0.Size, 0)
    T0._content = '0123456789'
    self.assertEqual(T0.Size, 10)
    T0._content = ''
    T0 = self.fs.get(('X', 'A', 'B', 'D', 'T0'))
    self.assertEqual(T0.Size, 0)

  def test_Size__folder(self):
    # empty folder
    E = self.fs.get(('X', 'E'))
    self.assertEqual(E.Size, 0)
    # folder with empty text-file
    D = self.fs.get(('X', 'A', 'B', 'D'))
    self.assertEqual(D.Size, 0)
    # folder with multiple text files
    C = self.fs.get(('X', 'A', 'B', 'C'))
    self.assertEqual(C.Size, 10)
    # folder with sub-folders
    B = self.fs.get(('X', 'A', 'B'))
    self.assertEqual(B.Size, 10)
    # folder with single text-file (changed)
    T0 = self.fs.get(('X', 'A', 'B', 'D', 'T0'))
    T0._content = '0123456789'
    self.assertEqual(D.Size, 10)
    # folder with sub-folders (changed)
    self.assertEqual(B.Size, 20)

  def test_Size__zip(self):
    # zipped text file
    ZZ = self.fs.get(('X', 'A', 'Z', 'ZZ'))
    self.assertEqual(ZZ.Size, 5)
    # zipped zip + text
    Z = self.fs.get(('X','A', 'Z'))
    self.assertEqual(Z.Size, 5.5)
    # folder containing a zip file (and other stuff)
    A = self.fs.get(('X', 'A'))
    self.assertEqual(A.Size, 15.5)

  def test_Size__zip__empty(self):
    self.fs.Create('drive', 'Z', None)
    # empty zip file
    self.fs.Create('zip', 'Z1', 'Z')
    Z1 = self.fs.get(('Z', 'Z1'))
    self.assertEqual(Z1.Size, 0)
    # zip file with empty text file
    self.fs.Create('text', 'Tz', 'Z\\Z1')
    self.assertEqual(Z1.Size, 0)
    # zip file with empty folder
    self.fs.Create('zip', 'Z2', 'Z')
    self.fs.Create('folder', 'F', 'Z\\Z2')
    Z2 = self.fs.get(('Z', 'Z2'))
    self.assertEqual(Z2.Size, 0)
    # zip file with empty zip file
    self.fs.Create('zip', 'Z3', 'Z')
    self.fs.Create('zip', 'Z4', 'Z\\Z3')
    Z3 = self.fs.get(('Z', 'Z3'))
    self.assertEqual(Z3.Size, 0)

  def test_Size__drive(self):
    X = self.fs.get(('X',))
    Y = self.fs.get(('Y',))
    # empty drive
    self.assertEqual(Y.Size, 0)
    # non-empty drive
    self.assertEqual(X.Size, 15.5)
  # endregion