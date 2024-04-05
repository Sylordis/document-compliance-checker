import yaml
from .exceptions.configurationfileerrorexception import ConfigurationFileErrorException

class DocumentComplianceConfiguration():

  def __init__(self):
    self.local_directory = None
    self.additional_columns = []

  def config_from_file(self, file : str):
    with open(file, 'r') as config_file:
      yaml_content = yaml.safe_load(config_file)
      if 'config' in yaml_content:
        for k,v in yaml_content['config'].items():
          if 'localdirectory' in k:
            self.local_directory = yaml_content['config']['localdirectory']
          if 'addcolumns' in k:
            self.additional_columns = yaml_content['config']['addcolumns']
      else:
        raise ConfigurationFileErrorException('Configuration file is badly formatted, should contain root "config".')

  def has_local_download(self) -> bool:
    return self.local_directory != None
  
  def has_additional_columns(self) -> bool:
    return len(self.additional_columns) != 0
