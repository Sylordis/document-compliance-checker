from abc import ABC, abstractmethod
from .compliancedocument import ComplianceDocument

class ComplianceCriterion(ABC):
  """Base interface for compliance criteria, which are predicates, taking one document and verifying the compliance to it."""

  def __init__(self, name : str, error : str):
    """Defines a new compliance criterion

    Parameters
    ----
    name: str
      Name of the criterion.
    error: str
      Message if this criterion is not respected.
    """
    self.name = name
    self.error = error

  @abstractmethod
  def validate(self, doc: ComplianceDocument) -> bool:
    """Predicate method validating this criterion against the document."""
    pass
