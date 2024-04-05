from abc import ABC

class ComplianceDocument(ABC):
  """Abstract class for documents managed by the compliance checker."""

  def __init__(self, title : str):
    self.title = title
