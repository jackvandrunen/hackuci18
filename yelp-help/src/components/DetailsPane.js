import React from 'react'
import './DetailsPane.css'
import PropTypes from 'prop-types'
import request from 'request'

const DetailsPane = (props) => {
    const my_id = props.match.params.place
    // try {
    //     var options = { method: 'GET',
    //       url: 'http://localhost:8080/lookup/',
    //       qs: {id : my_id}
    //     };
  
    //   request(options, function (error, response, body) {
    //     if (error) throw new Error(error);
    //     var json = JSON.parse(body)
    //     console.log(json)
    //   });
    // } catch (e) {
    //     console.log(e)
    // }
    try {
        var options = { method: 'GET',
          url: 'http://localhost:8080/lookup/',
          qs: {id : my_id}
        };
  
      request(options, function (error, response, body) {
        if (error) throw new Error(error);
        //Begin request to Jack using raw body
        try {
            var options = { method: 'GET',
              url: 'http://localhost:8181//',
              qs: {reviews : body}
            };
      
          request(options, function (error, response, body) {
            if (error) throw new Error(error);
            var jack_json = JSON.parse(body)
            console.log(jack_json)
            //end request to jack
            
          });
        } catch (e) {
            console.log(e)
        }
      });
    } catch (e) {
        console.log(e)
    }

    if (props.match.params.place !== '') {
        return (
            <div className='details-pane-container'>
                 <div className="details-pane">
                    <h2>{props.match.params.place}</h2>
                </div> 
            </div>
        )
    } else {
        return (
            <div className ="details-pane-container">
                <h2>Right Text</h2>
            </div>
        )       
    }
}

DetailsPane.PropTypes = {
    loading: PropTypes.bool.isRequired,
}

export default DetailsPane