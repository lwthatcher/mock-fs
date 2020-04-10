"""module for defining the multiple file-system 'entity' types"""
# TODO: possibly move to its own package later?

class FS_Entity:
  """base class for other entities, should not be used directly"""
  # region [Constructor]
  def __init__(self, _type, name, path):
    self.name = name
    self.path = path
  # endregion

  # region [Properties]
  @property
  def Type(self):
    return self._type

  @property
  def Name(self):
    return self.name
  
  @property
  def Path(self):
    return self.path

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


class FolderEntity(FS_Entity):
  # region [Constructor]
  def __init__(self, name, path):
    super.__init__('folder', name, path)
  # endregion

  # region [Implementation Methods]
  def _compute_size(self):
    # TODO: implement
    return 0
  # endregion