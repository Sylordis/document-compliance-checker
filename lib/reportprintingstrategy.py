from abc import ABC, abstractmethod
from .documentcompliancereport import DocumentComplianceReport
from .compliancestrategy import ComplianceStrategy

class ReportPrintingStrategy(ABC):
  """Interface for reports output. It's main method :py:meth:`~reportprintingstrategy.ReportPrintingStrategy.output` will create the report once called."""

  @abstractmethod
  def output(self, compliance_strategy : ComplianceStrategy, reports : list[DocumentComplianceReport], target : str):
    """Base method to output a report."""
    pass
