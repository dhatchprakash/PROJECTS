import configparser
import os

class DBPropertyUtil:
    @staticmethod
    def get_property_string(filename: str) -> str:
        print(f"Reading from file: {os.path.abspath(filename)}")

        config = configparser.ConfigParser()
        config.read(filename)

        # Debug print to see what sections were loaded
        print(" Loaded config sections:", config.sections())

        db_config = config['DATABASE']  # This line will throw error if [DATABASE] not found

        
        print(" Hostname:", db_config['hostname'])
        print(" Database Name:", db_config['dbname'])

        conn_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={db_config['hostname']};"
            f"DATABASE={db_config['dbname']};"
            f"Trusted_Connection=yes;"
        )
        return conn_string


if __name__ == "__main__":
    print("This is a utility module. Please import it instead of running directly.")
