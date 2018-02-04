import React from 'react'
import './DetailsPane.css'
import PropTypes from 'prop-types'
import request from 'request'

const DetailsPane = (props) => {
    const my_id = props.match.params.place
    try {
        var options = { method: 'GET',
          url: 'http://localhost:8080/lookup/',
          qs: {id : my_id}
        };
  
      request(options, function (error, response, body) {
        if (error) throw new Error(error);
        var json = JSON.parse(body)
        var food_info = json[1]
        return (
            <div className='details-pane-container'>
                    <div className="details-pane">
                    <h2>food_info[0][0]</h2>
                    <h2>food_info[0][1]</h2>
                </div> 
            </div>
        )
      });
    } catch (e) {
        console.log(e)
    }
}

DetailsPane.PropTypes = {
    loading: PropTypes.bool.isRequired,
}

export default DetailsPane