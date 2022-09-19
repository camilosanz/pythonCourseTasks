from datetime import datetime

def get_timestamp_string_hours():
    return datetime.now().strftime("%Y%m%d%H%M%S")

def get_timestamp_string():
    return datetime.now().strftime("%Y%m%d")

def get_filename(prefix="log", extension="txt"):
    """
    Builds filename using ``prefix`` string and ``sufix`` string 
    build from  timestamp yyyymmddHHMMSS
    output is: ``prefix_sufix.extension``
    """
    return "{}_{}.{}".format(prefix, get_timestamp_string_hours(), extension)


