# Yelp API Requests and BeautifulSoup to Retrieve All Reviews of a Business

import requests
from bs4 import BeautifulSoup
import json
import yelp_api_exception

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


def get_business_yelp_url(business_id: str) -> str:
    '''
    Builds business's Yelp URL.
    '''
    return "https://yelp.com/biz/" + business_id


# GET FUNCTIONS TO BE USED
def get_business_json_data(business_id: str) -> dict:
    '''
    Returns JSON data of a certain business.
    '''
    try:
        response = requests.request('GET', format_business_url(business_id), headers=HEADERS)
        return response.json()
    except:
        raise yelp_api_exception.YelpAPIException()


def get_search_json_data(terms: str, location: str) -> dict:
    '''
    Returns JSON data with search terms and location.
    '''
    try:
        search_terms = {
            'term': terms.replace(' ', '+'),
            'location': location.replace(' ', '+'),
            'limit': SEARCH_LIMIT,
            'categories': "food,All,restaurants,All"
        }
        response = requests.request('GET', format_search_url(), headers=HEADERS, params=search_terms)
        return response.json()
    except:
        raise yelp_api_exception.YelpAPIException()


def get_reviews_json_data(business_id: str) -> dict:    # ONLY ABLE TO RETRIEVE THREE REVIEWS SORTED BY YELP'S ALGORITHM
    '''
    Returns JSON data of only THREE reviews based on a business ID.
    '''
    try:
        response = requests.request('GET', format_reviews_url(business_id), headers=HEADERS)
        return response.json()
    except:
        raise yelp_api_exception.YelpAPIException()


def get_all_reviews_json_data(business_id: str) -> dict:    # USES BEAUTIFULSOUP TO RETRIEVE JSON FROM BUSINESS YELP SITE HTML
    '''
    Returns JSON data of all reviews from a business's Yelp website HTML using BeautifulSoup.
    '''
    try:
        html_response = requests.get(get_business_yelp_url(business_id)).text
        soup = BeautifulSoup(html_response, "lxml")
        data = str(soup.findAll('script', type="application/ld+json")[0].string)    # Retrieves text between specified tag
        data = data.strip()     # Gets rid of white space on ends of string
        return json.loads(data)
    except:
        raise yelp_api_exception.YelpAPIException()


# # TESTING PURPOSES ONLY
# TESTING PURPOSES ONLY
# if __name__ == "__main__":
#     print(get_business_json_data('pizza-hut-irvine-3'))
#     print(get_reviews_json_data('pizza-hut-irvine-3'))
#     print(get_search_json_data("computers", "Irvine, CA"))
#     print(get_all_reviews_json_data('pizza-hut-irvine-3'))