"""module for defining the multiple file-system 'entity' types"""

# expose only the main concrete file-system entities
from .folder import Folder, Drive
from .text import TextFile
from .zip import ZipFile

# map from entity names to their appropriate class
_ENTITIES = {'drive': Drive, 
  'folder': Folder,
  'text': TextFile,
  'zip': ZipFile}

# list of valid entity types
ENTITY_TYPES = _ENTITIES.keys()

# convenience method for creating appropriate entity types
def entity(fs, _type, full_path):
  return _ENTITIES[_type](fs, full_path)
