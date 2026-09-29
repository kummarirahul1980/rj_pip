import json
from pathlib import Path

def save_to_config(data):
    # Create a hidden folder in the user's home directory
    config_dir = Path.home() / ".rj_data"
    config_dir.mkdir(exist_ok=True)
    
    file_path = config_dir / "settings.json"
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    return str(file_path)