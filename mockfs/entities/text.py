"""module containing the text-file entity type"""
from .base import FS_Entity


class TextFile(FS_Entity, TYPE='text'):
  # region [Constructor]
  def __init__(self, fs, full_path):
    super().__init__(fs, full_path)
    self._content = ""
  # endregion

  # region [Properties]
  @property
  def Content(self):
    return self._content
  # endregion

  # region [Public Methods]
  def write(self, content):
    # coerce to string in case non-string input is accidently provided
    self._content = str(content)
  # endregion

  # region [Overrides Methods]
  def _compute_size(self):
    return len(self._content)
  # endregion
