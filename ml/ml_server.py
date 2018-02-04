# # Bottle server for searches and lookups on Yelp API

# import bottle
# import yelp_api

# @bottle.route('/search/')
# def search_results():
#     search_terms = bottle.request.query.terms       # Reads query "terms" and "location"
#     location     = bottle.request.query.location
#     return yelp_api.get_search_json_data(search_terms, location)


# bottle.run(host='localhost', port=8080, debug=True)    # TURN DEBUG TO FALSE FOR LIVE VERSION

import bottle
import ml
import json

@bottle.route('/menu/', method='GET')
def search_results():
    try:
        reviews = json.loads(bottle.request.query.reviews)
    except Exception:
        reviews = []
    response, code = ml.menu_response(reviews)
    bottle.response.status = code
    bottle.response.content_type = 'application/json'
    return json.dumps(response)

bottle.run(host='localhost', port=8181, debug=True)    # TURN DEBUG TO FALSE FOR LIVE VERSION
