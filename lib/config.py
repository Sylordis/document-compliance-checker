# loaded config
conf = {
    "CONFIG_FILE" : "config.yaml"
}

class Config(object):
    """Configuration manager for the software."""
    def __init__(self):
        self._config = conf # set it to conf

    def get_property(self, property_name):
        if property_name not in self._config.keys(): # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]
    
    def get_configuration_file(self):
        return self.get_property('CONFIG_FILE')
