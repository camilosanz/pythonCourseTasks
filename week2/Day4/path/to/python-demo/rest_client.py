import requests

URL = 'https://demo-api.free.beeceptor.com/my/api/path'

def get_demo_api_data():
    """
    GET data from REST API endpoint
    """

    response = requests.get(URL)

    if response.status_code != 200:
        ##TODO: add a logger (tener informacion historica de la ejecucion)
        # en lugar de un print voy a hacer un log.info
        print(f'Request returned non OK value {response.status_code}')
        return
        
    return response.text
