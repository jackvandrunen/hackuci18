import React from 'react'
import './ListItem.css'

class ListItem extends React.Component {
    render () {
        const name = this.props.restaurant.name 
        const containerClasses = 'result-list-item-container'
        //Todo: ternary

        return (
            <div className={containerClasses}>
                <div className="result-list-item">
                    <div className="result-list-item-description">
                        <h2>{name}</h2>
                        <p>{this.props.restaurant.location.display_address}</p>
                    </div>
                </div>
            </div>
        )
    }
}

export default ListItem