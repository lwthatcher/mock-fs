"""simple utility module containing common functions and custom Errors"""

class NotATextFileError(Exception):
  pass

class IllegalFileSystemOperationError(Exception):
  pass


def split_path(path):
  """splits the provided path elements into a tuple"""
  if isinstance(path, str):
    path = path.split('\\')
  return tuple(path)
