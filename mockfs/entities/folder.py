"""module for the Folder and Drive entities"""
from .base import ContainerEntity


class FolderEntity(ContainerEntity, TYPE='folder'):

  def __init__(self, fs, full_path):
    super().__init__( fs, 'folder', full_path)


# The drive entity is included in this module rather than its own,
# since the main semantic difference between a folder and a drive
# is that a drive is a top-level folder.
class DriveEntity(ContainerEntity, TYPE='drive'):

  def __init__(self, fs, full_path):
    super().__init__(fs, 'drive', full_path)
