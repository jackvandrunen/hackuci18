import React from 'react'
import './Search.css'
import SearchBar from './SearchBar'
import PropTypes from 'prop-types'

class Search extends React.Component {
    constructor() {
        super()

        this.state = {
            shrink: false
        }
    }

    setShrink = (shrink) => {
        this.setState({shrink})
    }

    render() {
        const classes = !this.state.shrink ? 'search-container' : 'search-container-small'
        return (
            <div className={classes}>
                <SearchBar
                    updateSearchTerm={this.props.updateSearchTerm}
                />
            </div>
        )
    }
}
Search.PropTypes = {
    updateSearchTerm: PropTypes.func.isRequired
}

export default Search