"""module for the zip-file entity type"""
from .base import ContainerEntity


class ZipFile(ContainerEntity, TYPE='zip'):
  # region [Constructor]
  def __init__(self, fs, full_path):
    super().__init__(fs, full_path)
  # endregion

  # region [Overrides Methods]
  def _compute_size(self):
    unzipped_size = super()._compute_size()
    return unzipped_size / 2
  # endregion
