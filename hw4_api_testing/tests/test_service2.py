import pytest
import requests


@pytest.mark.parametrize("brewery_type", ["micro",
                                          "nano",
                                          "regional",
                                          "brewpub",
                                          "large",
                                          "planning",
                                          "bar",
                                          "contract",
                                          "proprietor",
                                          "closed"])
def test_filter_by_type(service2_brewery_url, brewery_type):
    """Check the filter of breweries by type if the brewery has it"""
    response = requests.get(service2_brewery_url + "?by_type=" + brewery_type)
    for x in response.json():
        if "brewery_type" in x:
            assert x["brewery_type"] == brewery_type


@pytest.mark.parametrize("country", ["United States", "Canada"])
def test_search_by_country(service2_brewery_url, country):
    response = requests.get(service2_brewery_url + "/search?query=" + country)
    for x in response.json():
        assert x["country"] == country


def test_check_max_per_page(service2_brewery_url):
    """Check the maximum number of items on  a page"""
    response = requests.get(service2_brewery_url + "?per_page=51")
    assert len(response.json()) == 50


def test_check_default_per_page(service2_brewery_url):
    """Check the default number of items on  a page"""
    response = requests.get(service2_brewery_url + "?per_page")
    assert len(response.json()) == 20


def test_get_single_brewery_by_id(service2_brewery_url):
    """Check that we get single brewery with an id set in request url"""
    breweries = requests.get(service2_brewery_url)
    for x in breweries.json():
        single_brewery = []
        brewery_id = x["id"]
        response = requests.get(service2_brewery_url + "/" + brewery_id)
        single_brewery.append(response.json())
        assert len(single_brewery) == 1
        assert response.json()["id"] == brewery_id


def test_check_status_code(service2_brewery_url):
    """Check that status code of an existing url is 200"""
    response = requests.get(service2_brewery_url)
    assert response.status_code == 200
    