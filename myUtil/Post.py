import requests


def get_post(url, input_json):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.163 Safari/537.36'
    }
    response = requests.post(url=url, headers=headers, json=input_json).json()
    if response['msg'] == 'true':
        return True
    else:
        return False


def get_contracts(url, input_json):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.163 Safari/537.36'
    }
    response = requests.post(url=url, headers=headers, json=input_json).json()
    return response


def get_filenames(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.163 Safari/537.36'
    }
    response = requests.post(url=url, headers=headers).json()
    return response
