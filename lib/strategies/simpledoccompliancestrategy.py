from ..compliancestrategy import ComplianceStrategy
from ..criteria import CriterionHasCover

class SimpleDocComplianceStrategy(ComplianceStrategy):

  def __init__(self):
    super().__init__()
    self.criteria = {
      'Cover' : [ CriterionHasCover('Document does not have a cover page.') ],
      'Header' : [],
      'Footer' : [],
      'Attribution Marking' : [ ]
    }
