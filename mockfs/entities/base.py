"""module for defining the multiple file-system 'entity' types"""
import os

class FS_Entity:
  """Base class for other entities, should not be used directly.

  A proper subclass must include the TYPE=<type> in the class definition.
  This avoids passing the type through the constructor.

  Example:
    class ImageFile(FS_Entity, TYPE='image'):
      ...
  """
  # region [Constructor]
  def __init__(self, fs, full_path):
    """
    Arguments:
      fs - the MockFileSystem object containing this entity
      full_path - a list-like seperating out each path element,
        with the last element being the name of the entity
    """
    self._fs = fs
    self._full_path = full_path  # assume a tuple

  @classmethod
  def __init_subclass__(cls, TYPE='?', **kwargs):
    """Called from the class defition of implementing sub-classes.
    
    Note that TYPE is added as a keyword argument 
    to avoid inheritance issues with intermediate abstract classes,
    such as ContainerEntity.
    """
    cls.TYPE = TYPE
    super().__init_subclass__(**kwargs)
  # endregion

  # region [Properties]
  @property
  def Type(self):
    return self.TYPE

  @property
  def Name(self):
    return self._full_path[-1]
  
  @property
  def Path(self):
    return '\\'.join(self._full_path)

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
    return self._fs.get_children(self._full_path)
  # endregion

  # region [Implementation Methods]
  def _compute_size(self):
    size = 0
    for c in self.children:
      size += c.Size
    return size
  # endregion

