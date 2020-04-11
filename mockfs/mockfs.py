"""contains container class for basic mock file system access"""
import os
from .util import IllegalFileSystemOperationError

# currently supported entity types
ENTITY_TYPES = ('drive', 'folder', 'text', 'zip')


class MockFileSystem:

  # region [Constructor]
  def __init__(self):
    # TODO: possibly allow basic initialization for debugging?
    self._entities = {}
  # endregion

  # region [Properties]
  @property
  def entities(self):
    # TODO: possible map from internal list to proper entity objects?
    return self._entities
  # endregion

  # region [Public Methods]
  def Create(self, _type, name, path):
    """Creates an entity of the specified type in the mock file-system.
    Arguments:
      _type -- the entity type to create (must be one of ENTITY_TYPES)
      name -- the name to give the specified entity
      path -- the path to the parent entity, use None for drives
    Raises:
        FileNotFoundError -- when the parent directory/entity cannot be found
        FileExistsError -- an entity with the given name and parent already exists
        IllegalFileSystemOperationError
    """
    # ensure provided type is valid
    if _type not in ENTITY_TYPES:
      msg = 'Unsupported type: "{}"'.format(_type)
      raise IllegalFileSystemOperationError(msg)
    # check valid location/name
    # create entity
    # add entity to registry

  def Delete(self, path):
    """Deletes the entity at the specified path
    Arguments:
      path -- the path to the entity to delete
    Raises:
      FileNotFoundError -- the target entity cannot be found
    """
    pass

  def Move(self, src, dest):
    """Changes the parent of an entity.

    Arguments:
      src -- the source entity's current path
      dest -- the target destination of the new path if successful
    
    Raises:
      FileNotFoundError
      FileExistsError
    """
    pass

  def WriteToFile(self, path, content):
    """Writes content to a text file.
    
    Arguments:
      path -- the path to the text file to write to
      content -- the content to be written to the text file. 
        This will overwrite any content already there.
    
    Raises:
      NotATextFileError
    """
    pass
  # endregion

  # region [Helper Methods]
  def get(self, path):
    return self._entities.get[path]
  # endregion
