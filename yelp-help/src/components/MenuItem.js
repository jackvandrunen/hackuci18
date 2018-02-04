import React from 'react'
import './MenuItem.css'

class MenuItem extends React.Component {
    constructor(props) {
        super(props)
    }

    render () {
        console.log("please")
        const item = this.props.info[0]
        const rating = this.props.info[1]
        console.log(item)
        const containerClasses = 'menu-list-item-container'
        return (
            <div className={containerClasses}>
                <div className="menu-list-item">
                    <div className="menu-list-item-name">
                        <h2>{item}</h2>
                    </div>
                    <div className="menu-list-item-rating">
                        <h2>{rating}</h2>
                    </div>
                </div>
            </div>
        )
    }
}

export default MenuItem