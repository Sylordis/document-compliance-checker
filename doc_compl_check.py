import argparse, logging, os, sys
from lib.documentcompliancechecker import DocumentComplianceChecker
from lib.documentcomplianceconfiguration import DocumentComplianceConfiguration
from lib.config import Config
# Documents specific, TODO to make it loadable from configuration
from lib.strategies.simpledoccompliancestrategy import SimpleDocComplianceStrategy
from lib.ingesters.simpledocingester import SimpleDocIngester
from lib.exporters.simpledocreportprinter import SimpleDocReportPrinter

def set_logger(newlvl : str):
  if newlvl and newlvl.casefold() in ('trace', 'debug', 'info', 'warn', 'error'):
    lvl = newlvl.upper()
  else:
    lvl = 'INFO'
  logging.basicConfig(level=lvl, encoding='utf-8', format='%(levelname)s: %(message)s')

def main() -> int:
  """Runs the software in order to check documents compliance."""
  cfg = Config()
  parser = argparse.ArgumentParser(prog=os.path.basename(__file__),
                                   description='Document compliance checker: This program checks the compliance of a list of documents regarding their format and specific mentions.')
  parser.add_argument('srcfile', help='csvfile to parse containing all files to process. Format of the file is "path,filename".')
  parser.add_argument('target', help='Output target file.')
  parser.add_argument('-l', '--download', action='store', help='Download the files locally to TMP if they are not located on the same partition, before checking compliance. Delete this directory once processed.', metavar='TMP')
  parser.add_argument('--log', action='store', help='Set the log level in: TRACE, DEBUG, INFO, WARN, ERROR. Default is INFO.', metavar='LEVEL')
  parser.add_argument('--cfg', action='store', help=f"Specify a configuration file. Default takes \"{cfg.get_configuration_file()}\" if not specified.", metavar='FILE')
  args = parser.parse_args()
  ps_ret = 0
  set_logger(args.log)
  # Check that list file is accessible
  if os.path.isfile(args.srcfile) and os.access(args.srcfile, os.R_OK):
    doc_cfg = DocumentComplianceConfiguration()
    # Start compliance checking
    logging.info('Compliance checker start')
    # Set configuration
    if os.path.isfile(cfg.get_configuration_file()) and os.access(cfg.get_configuration_file(), os.R_OK):
      doc_cfg.config_from_file(cfg.get_configuration_file())
    else:
      logging.warning(f"Couldn't access or read configuration file '{cfg.get_configuration_file()}'. Not defined?")
    # Check if download variable is set (only set if option has been used)
    if 'download' in locals():
      logging.warning('Local download is set.')
      doc_cfg.local_directory = download
    checker = DocumentComplianceChecker(doc_cfg)
    checker.load_file_list(SimpleDocIngester(), args.srcfile)
    checker.create_compliance_reports(SimpleDocComplianceStrategy())
    checker.print_reports(SimpleDocReportPrinter(doc_cfg), args.target)
    logging.info(f"Compliance checker finished, report can be found at {args.target}")
  else:
    logging.error(f"File {args.srcfile} cannot be found or is not readable")
    ps_ret = 1
  return ps_ret

if __name__ == '__main__':
  sys.exit(main())
