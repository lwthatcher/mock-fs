"""module for defining the multiple file-system 'entity' types"""

# expose only the main concrete file-system entities
from .folder import Folder, Drive
from .text import TextFileEntity
from .zip import ZipFileEntity

# map from entity names to their appropriate class
_ENTITIES = {'drive': Drive, 
  'folder': Folder,
  'text': TextFileEntity,
  'zip': ZipFileEntity}

# list of valid entity types
ENTITY_TYPES = _ENTITIES.keys()

# convenience method for creating appropriate entity types
def entity(fs, _type, full_path):
  return _ENTITIES[_type](fs, full_path)
