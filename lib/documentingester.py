from abc import ABC, abstractmethod
from .compliancedocument import ComplianceDocument

class DocumentIngester(ABC):

  @abstractmethod
  def ingest_file(self, file:str) -> ComplianceDocument:
    """Ingests a file from a path and returns a document type"""
    pass
