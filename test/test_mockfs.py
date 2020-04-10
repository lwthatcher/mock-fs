from unittest import TestCase
from mockfs import MockFileSystem

class TestMockFileSystem(TestCase):
  
  def test_constructable(self):
    fs = MockFileSystem()

