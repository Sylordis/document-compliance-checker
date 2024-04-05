import os

def same_partition(f1, f2) -> bool:
  """Checks if two files are located on the same partition."""
  return os.stat(f1).st_dev == os.stat(f2).st_dev
