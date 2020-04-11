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
  """file-system abstract entity for parent entities"""
  # region [Properties]
  @property
  def children(self):
    # TODO: implement
    return []
  # endregion

  # region [Implementation Methods]
  def _compute_size(self):
    # TODO: implement
    return 0
  # endregion

