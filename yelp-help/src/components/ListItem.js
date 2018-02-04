import React from 'react'
import './ListItem.css'
import PropTypes from 'prop-types'
import { Redirect } from 'react-router'

class ListItem extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            redirect: false
        }
    }

    handleSelect = (event) => {
       this.setState({redirect: true})
    }

    render () {
        const name = this.props.restaurant.name 
        const id = this.props.restaurant.id
        const containerClasses = 'result-list-item-container'
        if (this.state.redirect) {
            return <Redirect to={{
                pathname: '/details/' + id,
              }}/>
        }
        return (
            <div className={containerClasses}>
                <div className="result-list-item" onClick={this.handleSelect}>
                    <div className="result-list-item-description">
                        <h2>{name}</h2>
                        <p>{this.props.restaurant.location.display_address}</p>
                    </div>
                </div>
            </div>
        )
    }
}

ListItem.PropTypes = {
}

export default ListItem