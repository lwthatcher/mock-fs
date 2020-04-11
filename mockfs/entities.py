"""module for defining the multiple file-system 'entity' types"""
import os

class FS_Entity:
  """base class for other entities, should not be used directly"""
  # region [Constructor]
  def __init__(self, fs, _type, full_path):
    self._fs = fs
    self._type = _type
    self._full_path = full_path  # assume a tuple
  # endregion

  # region [Properties]
  @property
  def Type(self):
    return self._type

  @property
  def Name(self):
    return self._full_path[-1]
  
  @property
  def Path(self):
    return self._full_path[:-1].join('/')

  @property
  def Size(self):
    return self._compute_size()
  # endregion

  # region [Abstract Methods]
  def _compute_size(self):
    """Computes the size this item should have.

    The abstract implementation raises an error
    rather than returning a dummy value (such as 0)
    to make it clear it is the implementing class's job
    to handle this correctly.

    """
    raise NotImplementedError
  # endregion


class ContainerEntity(FS_Entity):
  @property
  def children(self):
    return []

  def _compute_size(self):
    return 0


class FolderEntity(ContainerEntity):
  # region [Constructor]
  def __init__(self, fs, full_path):
    super().__init__( fs, 'folder', full_path)
  # endregion


class DriveEntity(ContainerEntity):
  # region [Constructor]
  def __init__(self, fs, full_path):
    super().__init__(fs, 'drive', full_path)
  # endregion


class TextFileEntity(FS_Entity):
  # region [Constructor]
  def __init__(self, fs, full_path):
    super().__init__(fs, 'text', full_path)
  # endregion


class ZipFileEntity(ContainerEntity):
  # region [Constructor]
  def __init__(self, fs, full_path):
    super().__init__(fs, 'zip', full_path)
  # endregion
