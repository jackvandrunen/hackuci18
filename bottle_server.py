# Bottle server for searches and lookups on Yelp API

import bottle
import yelp_api
import reviews
import requests
import json

API_HOST = "http://localhost"
ML_LOCAL_PORT = 8181


@bottle.hook('after_request')
def enableCORSAfterRequestHook():
    print ('After request hook.')
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'


@bottle.route('/search/', method='GET')
def search_results():
    search_terms = bottle.request.query.terms       # Reads query "terms" and "location"
    location     = bottle.request.query.location
    response     = yelp_api.get_search_json_data(search_terms, location)
    return response

# *********************************************************************************
def _retrieve_ml_json_data(business_id: str) -> json:   # Talks to ML server and retrieves JSON data
    params   = {'reviews': reviews.generate_review_text_json(yelp_api.get_all_reviews_json_data(business_id))}
    response = requests.get("{}:{}/menu/".format(API_HOST, ML_LOCAL_PORT), params=params)
    return response.json()


@bottle.route('/lookup/', method = 'GET')
def biz_lookup():
    business_id = bottle.request.query.id
    ml_reviews  = _retrieve_ml_json_data(business_id)
    return yelp_api.get_business_json_data(business_id), ml_reviews
# *********************************************************************************

@bottle.route('/ml_json/', method = 'GET')
def get_json_to_send_to_ml():
    return reviews.generate_review_text_json(yelp_api.get_all_reviews_json_data(bottle.request.query.id))


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)    # TURN DEBUG TO FALSE FOR LIVE VERSION
