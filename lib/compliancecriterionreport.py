from .compliancecriterion import ComplianceCriterion

class ComplianceCriterionReport:
  """Report of compliance for a single criterion."""

  def __init__(self, criterion : ComplianceCriterion):
    self.criterion : ComplianceCriterion = criterion
    self.compliant : bool = False
