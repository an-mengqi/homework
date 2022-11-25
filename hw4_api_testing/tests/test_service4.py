import requests


def test_check_status_code(url, status_code):
    """Running test with arguments --url and --status_code"""
    response = requests.get(url)
    assert str(status_code) == str(response.status_code)
