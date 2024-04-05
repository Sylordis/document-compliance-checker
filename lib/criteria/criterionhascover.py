from ..compliancecriterion import ComplianceCriterion
from ..compliancedocument import ComplianceDocument
import os.path

class CriterionHasCover(ComplianceCriterion):
  """This criterion checks if a document has cover page.
  A cover page is defined by a single page at the beginning of the document that has the title of the document on it.
  """

  def __init__(self, error : str = ''):
    super().__init__("Document has a cover page", error)

  def validate(self, doc: ComplianceDocument) -> bool:
    """Predicate method validating this criterion against the document."""
    validation = False
    match os.path.splitext(doc.path)[-1].lower():
      case 'docx':
        validation = self.validate_docx(doc)
      case 'xlsx':
        validation = self.validate_xlsx(doc)
    return validation

  def validate_docx(self, doc:ComplianceDocument) -> bool:
    """Check for cover page in Word document."""
    # TODO validate docx document
    return False

  def validate_xlsx(self, doc:ComplianceDocument) -> bool:
    """Check for cover page in Excel document.
    It is assumed to be the first sheet."""
    # TODO validate xlsx document
    return False
