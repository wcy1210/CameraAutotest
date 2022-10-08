import os
import time
import yaml

class Config_all:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
        self.report_path = os.path.join(self.base_path, 'report', 'sta_' + time.strftime('%y_%m_%d_%H_%M_%S', time.localtime()))
        self.resource_path = os.path.join(self.base_path, 'resource')
        self.config = self.get_config()

    def get_config(self):


    def get_defalt_yaml(self):
        print(self.report_path)

a = Config_all()
a.get_defalt_yaml()