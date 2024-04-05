from pathlib import PurePosixPath
from ..documents.simpledoc import SimpleDoc

class SimpleDocIngester():
  """Document ingester for simple documents"""

  def ingest_file(self, file:str) -> SimpleDoc:
    """Takes a path to create a simple document out of it"""
    document = SimpleDoc()
    document.path = file
    path = PurePosixPath(file).stem
    document.title = str(path)
    return document
