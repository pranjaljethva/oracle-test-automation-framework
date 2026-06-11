import yaml
import os


class ConfigReader:
    """Read and manage configuration from YAML files"""

    @staticmethod
    def get_project_path():
        curr_dir_path = os.getcwd()

        while not os.listdir(curr_dir_path).__contains__('requirements.txt'):
            curr_dir_path = os.path.dirname(os.path.abspath(curr_dir_path))
            print("Project Path is: " + curr_dir_path)

        return curr_dir_path

    @staticmethod
    def read_config(file_name):
        """
        Read YAML configuration file and return parsed data
        
        Args:
            config_file_name (str): Name of the YAML config file with extension
            
        Returns:
            dict: Parsed YAML configuration data
            
        """
        project_path = ConfigReader.get_project_path()
        print ("Project path in get reader is " + project_path)
        config_file_path = project_path + '/config/{}'.format(file_name)
        print ("Config file path is : " + config_file_path)
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"Config file not found: {config_file_path}")
        
        try:
            with open(config_file_path, 'r') as file:
                config_data = yaml.safe_load(file)
            return config_data
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
    
    @staticmethod
    def get_config_value(file_name, key):
        """
        Get a specific value from YAML config using nested keys
        
        Args:
            file_name (str): Name of the YAML config file
            key: Key name (e.g., 'qa', 'base_url')
            
        Returns:
            Value at the specified key, or None if not found
            
        """
        config_data = ConfigReader.read_config(file_name)
        print ("config data: " + config_data.__str__())

        env = config_data['environment']
        return config_data[env][key]

# Example usage:
# if __name__ == "__main__":
#     # config_path = os.path.join(os.path.dirname(__file__), '../config/base_config.yml')
#
#     # Read entire config
#     config = ConfigReader.read_config("base_config.yml")
#     print("Full config:", config)
#
#     # Get specific values
#     base_url = ConfigReader.get_config_value("base_config.yml", 'base_url')
#     print("QA Base URL:", base_url)
#
#     username = ConfigReader.get_config_value("base_config.yml", 'user_name')
#     print("QA Username:", username)
