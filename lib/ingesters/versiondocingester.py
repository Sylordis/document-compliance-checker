import logging
from pathlib import PurePosixPath
from ..documents.versiondoc import VersionDoc

class VersionDocIngester():
  """Document ingester for version documents"""

  def ingest_file(self, file:str) -> VersionDoc:
    """Takes a path to create a cdocument out of it"""
    document = VersionDoc()
    document.path = file
    path = PurePosixPath(file).stem
    parts = str(path).split('_')
    document.title = ' '.join(parts[4:])
    document.reference = parts[0]
    document.version = parts[3]
    logging.info(f"Document ingested: {document.reference} v{document.version}")
    return document
