from abc import ABC, abstractmethod
from .compliancecriterion import ComplianceCriterion
from .compliancedocument import ComplianceDocument
from .compliancecriterionreport import ComplianceCriterionReport
from .documentcompliancereport import DocumentComplianceReport

class ComplianceStrategy(ABC):
  """Interface for all compliance strategies"""

  def __init__(self):
    self.criteria : dict[str, list[ComplianceCriterion]] = {}

  def check_document_compliance(self, file : ComplianceDocument) -> DocumentComplianceReport:
    """Checks the compliance of the given document compared to the criteria, producing a report."""
    document_report = DocumentComplianceReport(file)
    # Loop through criteria categories
    for key, criteria in self.criteria.items():
      document_report.criteria_compliance[key] = []
      for criterion in criteria:
        criterion_report = ComplianceCriterionReport(criterion)
        criterion_report.compliant = criterion.validate(file)
        document_report.criteria_compliance[key].append(criterion_report)
    return document_report
