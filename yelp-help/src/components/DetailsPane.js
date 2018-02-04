import React from 'react'
import './DetailsPane.css'
import PropTypes from 'prop-types'
import request from 'request'
import MenuItem from './MenuItem'

class DetailsPane extends React.Component {
    constructor (props) {
        super(props)

        this.state = {
            requested: false,
            my_id: props.match.params.place,
            food_info: []
        }
    }

    //var my_id = props.match.params.place
    render() {
        if (this.state.my_id !== '' && !this.state.requested) {
            console.log(this.state.my_id)
            var my_app = this
            try {
                var options = { method: 'GET',
                  url: 'http://localhost:8080/lookup/',
                  qs: {id : my_app.state.my_id}
                };
              request(options, function (error, response, body) {
                if (error) throw new Error(error);
                var json = JSON.parse(body)
                my_app.setState({
                    food_info: json[1]
                })
                my_app.state.requested = true
                console.log(my_app.state.food_info)
              });
            } catch (e) {
                console.log(e)
            }
            return (<div className='menu_list_container'>
            <div className="menu-list">
                {this.state.food_info.forEach(element => {
                return (
                    <MenuItem info={element}/>
                    ) 
                })};
            </div> 
        </div>)
        } else if (this.state.requested) {
            console.log('Food info good!')
            return (<div className='menu_list_container'>
                    <div className="menu-list">
                        {this.state.food_info.forEach(element => {
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
                    <h2>Loading for {this.state.my_id}</h2>
                </div>
            )       
        }
    }
}

DetailsPane.PropTypes = {
    loading: PropTypes.bool.isRequired,
}

export default DetailsPane