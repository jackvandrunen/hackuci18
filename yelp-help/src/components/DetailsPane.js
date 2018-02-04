import React from 'react'
import './DetailsPane.css'
import PropTypes from 'prop-types'
import request from 'request'

const DetailsPane = (props) => {
    const my_id = props.match.params.place
    var food_info = ''
    
    try {
        var options = { method: 'GET',
          url: 'http://localhost:8080/lookup/',
          qs: {id : my_id}
        };
  
      request(options, function (error, response, body) {
        if (error) throw new Error(error);
        var json = JSON.parse(body)
        food_info = json[1]
      });
    } catch (e) {
        console.log(e)
    }

    if (food_info !== '') {
        return (
            <div className='details-pane-container'>
                 <div className="details-pane">
                    <h2>{food_info[0][0]}</h2>
                    <h2>{food_info[0][1]}</h2>
                </div> 
            </div>
        )
    } else {
        return (
            <div className ="details-pane-container">
                <h2>Loading for {props.match.params.place}</h2>
            </div>
        )       
    }
}

DetailsPane.PropTypes = {
    loading: PropTypes.bool.isRequired,
}

export default DetailsPane