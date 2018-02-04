import React from 'react'
import './MenuItem.css'

class MenuItem extends React.Component {
    constructor(props) {
        super(props)
    }

    render () {
        const item = this.props.info.item
        const rating = this.props.info.rating
        const containerClasses = 'menu-list-item-container'
        return (
            <div className={containerClasses}>
                <div className="menu-list-item">
                    <div className="menu-list-item-description">
                        <h2>{item}</h2>
                        <p>{rating}</p>
                    </div>
                </div>
            </div>
        )
    }
}

export default MenuItem