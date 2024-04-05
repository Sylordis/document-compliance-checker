import csv
import logging
import os
import shutil
from . import utils
from pathlib import Path, PurePath
from .documentingester import DocumentIngester
from .compliancestrategy import ComplianceStrategy
from .reportprintingstrategy import ReportPrintingStrategy
from .compliancedocument import ComplianceDocument
from .documentcompliancereport import DocumentComplianceReport
from .documentcomplianceconfiguration import DocumentComplianceConfiguration

class DocumentComplianceChecker:
  """Orchestrator for the compliance checks of multiple documents."""

  def __init__(self, doccfg : DocumentComplianceConfiguration, compliance_strategy: ComplianceStrategy = None):
    self.files : list[ComplianceDocument] = []
    self.reports : list[DocumentComplianceReport] = []
    self.compliance_strategy : ComplianceStrategy = compliance_strategy
    self.doccfg = doccfg

  def load_file_list(self, ingester : DocumentIngester, sourcefile : str):
    """Loads a list of files from a specific csv file. This file should have the format 'path,filename'."""
    logging.info(f"Ingesting file(s) described in {sourcefile}")
    with open(sourcefile,'r') as readfile:
      csv_file = csv.DictReader(readfile)
      # Check every line, skipping header
      for row in csv_file:
        abspath = Path(row['path'], row['filename']).absolute()
        logging.debug(msg=f"Checking '{abspath}'")
        # If file exists, ingest it
        if os.path.exists(abspath):
          self.files.append(ingester.ingest_file(abspath)) 
        else:
          logging.error("File does not exist or cannot be reached.")
      logging.info(f"Ingestion finished: {len(self.files)} file(s) ingested.")

  def create_compliance_reports(self, strategy: ComplianceStrategy):
    """Processes all documents to check compliance for each."""
    logging.info("Checking documents compliance")
    self.reports = []
    self.compliance_strategy = strategy
    # Check if local download
    if self.doccfg.has_local_download():
      logging.info("Checking documents that need to be downloaded locally")
      self.create_local_directory()
      # Check if files have to be downloaded
      for file in self.files:
        if not(utils.same_partition(__file__, file.path)):
          filename = PurePath(file.path).name()
          newpath = Path(self.doccfg.local_directory + '/' + filename)
          # Download document first if not on the same partition
          logging.info(f"Downloading {filename}")
          shutil.copyfile(file.path, newpath)
          logging.debug('File downloaded')
          # Change downloaded document's internal path
          file.path = newpath
    for file in self.files:
      self.reports.append(strategy.check_document_compliance(file))
    # If local download, delete temporary directory
    if self.doccfg.has_local_download():
      self.delete_local_directory()
    logging.info("Documents compliance established")

  def print_reports(self, strategy : ReportPrintingStrategy, target : str):
    """Print reports according to a strategy."""
    logging.info(f"Printing compliance report to {target}")
    strategy.output(self.compliance_strategy, self.reports, target)

  def create_local_directory(self):
      """Creates the local temporary directory to download remote files in it first."""
      logging.info("Creating temporary directory")
      Path(self.doccfg.local_directory).mkdir(exist_ok=True)
      logging.info("Temporary directory created")

  def delete_local_directory(self):
    """Deletes the local temporary directory and all files in it."""
    logging.info('Deleting temporary directory')
    if (Path(self.doccfg.local_directory).is_dir()):
      for file_name in Path(self.doccfg.local_directory).iterdir():
        file = Path(self.doccfg.local_directory + '/' + file_name)
        if file.is_file():
            file.unlink()
        Path(self.doccfg.local_directory).rmdir()
      logging.info('Temporary directory deleted')
    else:
      logging.error('Cannot delete temporary directory : it does not exist.')