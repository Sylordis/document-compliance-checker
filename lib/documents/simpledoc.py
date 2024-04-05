from ..compliancedocument import ComplianceDocument

class SimpleDoc(ComplianceDocument):
  """Represents a simple document."""

  def __init__(self, title : str = ''):
    super().__init__(title)

