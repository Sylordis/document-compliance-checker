from ..compliancedocument import ComplianceDocument

class VersionDoc(ComplianceDocument):
  """Represents a document with format <REFERENCE>_<ACRONYM>_<VERSION>_<TITLE>"""

  def __init__(self, title : str = '', reference : str = '', acronym : str = '', version : str = '', path : str = ''):
    super().__init__(title)
    self.reference = reference
    self.acronym = acronym
    self.version = version
    self.path = path

  def __str__(self):
    return f"{self.reference}, {self.acronym}, v{self.version}, \"{self.title}\""
