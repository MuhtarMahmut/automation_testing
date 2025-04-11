import json
from typing import Any, Dict, Union


class JsonUtilities:

    @staticmethod
    def read_json(file_path: str) -> Union[Dict, list, None]:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"[!] JSON file not found: {file_path}")
        except json.JSONDecodeError:
            print(f"[!] Invalid JSON format in file: {file_path}")
        except Exception as e:
            print(f"[!] Failed to read JSON file: {e}")
        return None

    @staticmethod
    def write_json(file_path: str, data: Union[Dict, list]) -> None:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"[!] Failed to write JSON to file: {e}")

    @staticmethod
    def update_json(file_path: str, updates: Dict[str, Any]) -> None:
        try:
            data = JsonUtilities.read_json(file_path)
            if data is None:
                return
            if isinstance(data, dict):
                data.update(updates)
                JsonUtilities.write_json(file_path, data)
            else:
                print("[!] JSON root is not a dictionary; cannot apply updates.")
        except Exception as e:
            print(f"[!] Failed to update JSON: {e}")

    @staticmethod
    def get_value(json_data: Dict[str, Any], key: str) -> Any:
        try:
            return json_data.get(key)
        except AttributeError:
            print(f"[!] Provided JSON data is not a dictionary.")
        return None
