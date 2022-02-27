import requests

def unprotected_page_status():
    page = requests.get('http://127.0.0.1:5000/')
    return page.status_code

def testing():
    assert unprotected_page_status() == 400

testing()
