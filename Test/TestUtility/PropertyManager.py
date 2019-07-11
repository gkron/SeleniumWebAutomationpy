import configparser

class PropertyManager():
    def __init__(self,properties_file_name):
        self.properties_file_name = properties_file_name
        self.config = configparser.RawConfigParser()
        self.config.read(properties_file_name)

    def get_property(self,property_name):
        #property_value = ''
        property_value = self.config.get('Properties', property_name.strip())
        return property_value
