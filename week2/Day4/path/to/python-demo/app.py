""" 
    Entry point for my application
"""

from utils import get_filename, get_timestamp_string
from rest_client import get_demo_api_data
from files_helper import write_data_in_file


def main():
    raw_data = get_demo_api_data()
    filename = get_filename()
    target_path = './to/' + get_timestamp_string()    
    write_data_in_file(raw_data, filename, target_path)

main()