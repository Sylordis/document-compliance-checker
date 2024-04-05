import csv
from ..reportprintingstrategy import ReportPrintingStrategy
from ..compliancestrategy import ComplianceStrategy
from ..documentcompliancereport import DocumentComplianceReport
from ..documentcomplianceconfiguration import DocumentComplianceConfiguration

class SimpleDocReportPrinter(ReportPrintingStrategy):
  """Printer for SimpleDoc compliance reports"""

  def __init__(self, cfg : DocumentComplianceConfiguration):
    self.cfg = cfg

  def output(self, compliance_strategy : ComplianceStrategy, reports : list[DocumentComplianceReport], target : str):
    with open(target, 'w', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      row = self.create_csv_header(compliance_strategy)
      csvwriter.writerow(row)
      # Loop through reports
      for report in reports:
        document = report.document
        messages = []
        # Prepare first columns with known information
        row=[document.title]
        # Loop through each entry critera category
        for key, criteria_category in report.criteria_compliance.items():
          # Category is compliant if all criteria are compliant
          compliant = all(map(lambda c : c.compliant, criteria_category))
          # Gather all non compliant criteria's messages
          messages_cat = list(map(lambda c : c.criterion.error, filter(lambda c : not(c.compliant), criteria_category)))
          row.append('y' if compliant else 'n')
          # If the category is not completely compliant, put the error messages after the category name
          if not(compliant):
            messages_cat.insert(0, f"{key}:")
          # Add all messages to overall messages
          messages = messages + messages_cat
        # Add empty fields from configuration
        row += map(lambda n : '', self.cfg.additional_columns)
        # Append all messages as comments
        row.append('\n'.join(messages))
        csvwriter.writerow(row)

  def create_csv_header(self, compliance_strategy: ComplianceStrategy) -> list[str]:
    row = ['Title']
    row += [key for key in compliance_strategy.criteria]
    row += self.cfg.additional_columns
    row += ['Compliance comments']
    return row