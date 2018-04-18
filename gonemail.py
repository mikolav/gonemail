import requests

_URL = "https://gonemail.net/api/v1/"

def get_mail(email_address, scope=['body', 'from', 'subject']):
    r = requests.post('{}inbox/{}?scope={}'.format(_URL, email_address, ','.join(scope)))
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(r.json()['error'])