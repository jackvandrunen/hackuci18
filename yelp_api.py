# Yelp API Reqeusts

import requests

API_HOST = "https://api.yelp.com"
API_KEY = "Y7tqjnvosHUlt_CzHiXINdMrzGJ5pAYAkpyNyFf-CVbOptscEN-wEYaqBeCiCcuO80FiRiC0UF71wMIA_ad1l4f7yRJ-WhWm9jzENIyl7ZKf7BqioZfQT2RBNVh1WnYx"
HEADERS = {'Authorization': "Bearer {}".format(API_KEY)}
SEARCH_LIMIT = 10

# HELPER METHODS TO FORMAT URLS
def format_business_url(business_id: str) -> str:
    '''
    Formats and returns the formatted URL to retrieve detailed business data.
    '''
    business_url = API_HOST + "/v3/businesses/{id}"
    return business_url.format(id=business_id)


def format_search_url() -> str:
    '''
    Formats and returns the formatted URL to retrieve businesses in a search.
    '''
    return API_HOST + "/v3/businesses/search"


def format_reviews_url(business_id: str) -> str:
    '''
    Formats and returns the formatted URL to retrieve business review information.
    '''
    return API_HOST + "/v3/businesses/{id}/reviews".format(id=business_id)


# GET FUNCTIONS TO BE USED
def get_business_json_data(business_id: str) -> (str, dict):
    '''
    Returns JSON data of a certain business.
    '''
    response = requests.request('GET', format_business_url(business_id), headers=HEADERS)
    return business_id, response.json()


def get_search_json_data(terms: str, location: str) -> dict:
    '''
    Returns JSON data with search terms and location.
    '''
    search_terms = {
        'term': terms.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    response = requests.request('GET', format_search_url(), headers=HEADERS, params=search_terms)
    return response.json()


def get_reviews_json_data(business_id: str) -> dict:
    '''
    Returns JSON data of reviews based on a business ID.
    '''
    response = requests.request('GET', format_reviews_url(business_id), headers=HEADERS)
    return response.json()


# TESTING PURPOSES ONLY
if __name__ == "__main__":
    print(get_business_json_data('pizza-hut-irvine-3'))
    print(get_reviews_json_data('pizza-hut-irvine-3'))
    print(get_search_json_data("pizza hut", "Irvine, CA"))