import pytest


@pytest.fixture
def service1_dog_breed_url():
    dog_breed_url = "https://dog.ceo/api/breed/"
    return dog_breed_url


@pytest.fixture
def service1_dog_ceo_url():
    dog_ceo_url = "https://dog.ceo"
    return dog_ceo_url


@pytest.fixture()
def service2_brewery_url():
    brewery_url = "https://api.openbrewerydb.org/breweries"
    return brewery_url


@pytest.fixture()
def service3_jsonplaceholder_url():
    jsonplaceholder_url = "https://jsonplaceholder.typicode.com/"
    return jsonplaceholder_url


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")
    parser.addoption("--status_code", default="200")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
