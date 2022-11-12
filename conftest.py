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
