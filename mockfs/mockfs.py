"""contains container class for basic mock file system access"""
import os
from .util import IllegalFileSystemOperationError, split_path
from .entities import ENTITY_TYPES, entity


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
      raise IllegalFileSystemOperationError('Unsupported type: "{}"'.format(_type))
    full_path = split_path(path, name)
    # ensure parents exist
    if not self.parents_exist(full_path):
      raise FileNotFoundError('The path to the specified item does not exist.')
    # ensure does not already exist
    if full_path in self._entities.keys():
      raise FileExistsError('The specified path already exists.')
    # ensure drives can only be top-level

    # ensure no nesting inside of text files
    # add entity to file-system registry
    item = entity(self, _type, full_path)
    self._entities[full_path] = item

  def Delete(self, path):
    """Deletes the file-system entity at the specified path.

    If the specified entity contains other entities,
    all child entities are also deleted.

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
    # Ensure the src file exists
    # Ensure the dest path does not already exist
    # change the path internally for the src file
    # change the path names for all children of the src file
    # add updated entity (and children) to _entities dict
    # remove old keys from entity dict
    pass

  def WriteToFile(self, path, content):
    """Writes content to a text file.
    Arguments:
      path -- the path to the text file to write to
      content -- the content to be written to the text file. 
        This will overwrite any content already there.
    Raises:
      FileNotFoundError
      NotATextFileError
    """
    pass
  # endregion

  # region [Helper Methods]
  def exists(self, full_path):
    return full_path in self._entities.keys()

  def get(self, full_path):
    return self._entities.get(full_path)

  def parents_exist(self, full_path):
    _p = full_path[:-1]  # parent path
    parents = [_p[:i+1] for i in range(len(_p))]  # paths for all ancestors
    exists = [p in self._entities.keys() for p in parents]  # bool array if exists
    return all(exists)

  def get_children(self, full_path):
    def childof(a, b):
      return a[:len(b)] == b and a != b  # a starts with b, but excludes b itself
    result = [v for k,v in self._entities.items() if childof(k, full_path)]
    return result
  # endregion
