from .compliancedocument import ComplianceDocument
from .compliancecriterionreport import ComplianceCriterionReport

class DocumentComplianceReport:
  """Base class to store compliance check reports for a single document."""

  def __init__(self, doc : ComplianceDocument):
    self.criteria_compliance : dict[str, list[ComplianceCriterionReport]] = {}
    self.document : ComplianceDocument = doc
