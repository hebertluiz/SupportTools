import json


class ConfigMan:

    config_array = {'hosts': 'path\\to\\hosts\\file',
                    'clients_dict': 'path\\to\\clients_dict',
                    'debug': 'True',
                    'ssh_bin': 'ssh '
                    }

    def __init__(self, config_path):

        try:
            with open(config_path + "support.json") as json_config_file:
                json_config = json_config_file.read()
                self.config_array = json.loads(json_config)

        except FileNotFoundError:
            print("File not found: ", config_path + "support.json")
            raise FileNotFoundError

    def get_opt(self, config_opt=None):

        if not config_opt or config_opt is None:
            return self.config_array.keys()

        elif config_opt not in self.config_array:
            print("Invalid option.", self.config_array.keys())

        else:
            return self.config_array[config_opt]

    def set_opt(self, config_opt, opt_value):
        if not config_opt:
            return False
        else:
            self.config_array[config_opt] = opt_value
            if self.get_opt(config_opt) == opt_value: return True
            else: return False

    def save_config(self, file_path):
        try:
            with open(file_path + "support.json",'w+') as out_file:
                json.dump(self.config_array, out_file, indent=4 , ensure_ascii=True)
        except FileNotFoundError:
            raise
