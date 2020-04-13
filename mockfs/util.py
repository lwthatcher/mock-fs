"""simple utility module containing common functions and custom Errors"""

class NotATextFileError(Exception):
  pass

class IllegalFSOpError(Exception):
  pass


def split_path(path, name=None):
  """Splits the provided path elements into a tuple.
  
  This method also handles the cases where path is already a tuple or a list.
  If name is provided, it will be appended to the end of the tuple.
  """
  # split apart path if non-empty string
  if path and isinstance(path, str):
    path = path.split('\\')
  # append name if present
  if name is not None:
    path = list(path or []) + [name]
  # return as a tuple
  return tuple(path)
