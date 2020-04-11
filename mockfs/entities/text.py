"""module containing the text-file entity type"""
from .base import FS_Entity


class TextFileEntity(FS_Entity):
  # region [Constructor]
  def __init__(self, fs, full_path):
    super().__init__(fs, 'text', full_path)
    self._content = ""
  # endregion

  # region [Properties]
  @property
  def Content(self):
    return self._content
  # endregion

  # region [Public Methods]
  def write(self, content):
    # TODO: add append kwarg option
    # coerce to string in case non-string input is accidently provided
    self._content = str(content)
  # endregion