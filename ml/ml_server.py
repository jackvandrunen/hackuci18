# # Bottle server for searches and lookups on Yelp API

import bottle
import ml
import json

@bottle.hook('after_request')
def enableCORSAfterRequestHook():
    print ('After request hook.')
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    

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
