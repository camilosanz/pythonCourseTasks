from utils import get_timestamp_string
from pathlib import Path
import os

def is_valid_path(path):
    if path is None:
        return False

    if path == '':
        return True

    obj = Path(path)
    if not obj.exists():
        os.mkdir(obj)
        print(f'{path} created!')
    else:
        print(f'{path} exists already!')
    
    return True

def build_full_filename(target_path, filename):
    return os.path.join(target_path, filename)

def write_data_in_file(data, filename, target_path):
    """
    Writes `data` in `filename`
    `filename` resides in `target_path` /path/to
    """
    if not is_valid_path(target_path):
        print(f"Error while validating target path: {target_path}")
        return
    
    filename = build_full_filename(target_path, filename)
    with open(filename, 'w') as openfile:
        openfile.write(data)