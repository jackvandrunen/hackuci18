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
            food_info: [],
            name: '',
            address:''
        }
        this.state.requested = false
    }

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
                console.log(json)
                my_app.setState({
                    name: json[0].name,
                    address: json[0].location.address1,
                    food_info: json[1]
                })
                my_app.state.requested = true
              });
            } catch (e) {
                console.log(e)
            }
            return (
                <div className ="menu-list-container">
                        <h2>Loading favorites for {this.state.my_id}...</h2>
                </div>)
        } else if (this.state.requested) {
            if (this.state.food_info.length > 0) {
                console.log("food found")
                return (<div className='menu_list_container'>
                <div className="menu-list">
                <h2> {this.state.name} at {this.state.address}</h2>
                    {this.state.food_info.map((item, index) => {
                        console.log(item)
                        return (
                            <MenuItem key={index} info={item} />
                        )
                    })}
                </div> 
            </div>)
            } else {
                console.log('Food info not found!')
                return (<div className='menu_list_container'>
                <div className="menu-list">
                    <h2> {this.state.name} </h2>
                    <h2> {this.state.address} </h2>
                    <h2> Not enough reviews! </h2>
                </div> 
            </div>)
            }
        }
    }
}

DetailsPane.PropTypes = {
    loading: PropTypes.bool.isRequired,
}

export default DetailsPane