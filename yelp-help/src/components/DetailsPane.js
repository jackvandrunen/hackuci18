import React from 'react'
import './DetailsPane.css'
import PropTypes from 'prop-types'
import request from 'request'
import MenuItem from './MenuItem'

const DetailsPane = (props) => {
    const my_id = props.match.params.place
    var food_info = {}
    
    try {
        var options = { method: 'GET',
          url: 'http://localhost:8080/lookup/',
          qs: {id : my_id}
        };
  
      request(options, function (error, response, body) {
        if (error) throw new Error(error);
        var json = JSON.parse(body)
        food_info = json[1]
        console.log(food_info)
      });
    } catch (e) {
        console.log(e)
    }

    if (food_info.length > 0) {
        console.log('Food info good!')
        // return (
        //     <div className='details-pane-container'>
        //          <div className="details-pane">
                 
        //         </div> 
        //     </div>
        // )
        return (<div className='menu_list_container'>
                 <div className="menu-list">
                    {food_info.forEach(element => {
                       return (
                        <MenuItem info={element}/>
                        ) 
                    })};
                </div> 
            </div>)
    } else {
        console.log("i hate food info!")
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