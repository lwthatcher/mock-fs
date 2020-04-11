"""module for defining the multiple file-system 'entity' types"""

# expose only the main concrete file-system entities
from .folder import FolderEntity, DriveEntity
from .text import TextFileEntity
from .zip import ZipFileEntity
