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
import yelp_api

@bottle.hook('after_request')
def enableCORSAfterRequestHook():
    print ('After request hook.')
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'

@bottle.route('/search/', method='GET')
def search_results():
    search_terms = bottle.request.query.terms       # Reads query "terms" and "location"
    location     = bottle.request.query.location
    return yelp_api.get_search_json_data(search_terms, location)

bottle.run(host='localhost', port=8080, debug=True)