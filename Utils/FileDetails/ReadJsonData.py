import json


class ReadJsonData():
    filepath = "C:\\Users\\DELL\\PycharmProjects\\August2025SeleniumPython\\EnvironmentDetails\\Env.json"

    def GetEnvironmentDetails(self):
        try:
            with open(self.filepath, 'r') as file:
                # Deserialize the file content into a Python object (typically a dictionary or list)
                data = json.load(file)
                print(data)
            return data
        except FileNotFoundError:
            print("Error: The file 'data.json' was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file (invalid JSON format).")

obj= ReadJsonData()
obj.GetEnvironmentDetails()
