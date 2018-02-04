import React from 'react'
import './SearchBar.css'
import PropTypes from 'prop-types'

class SearchBar extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            search: '',
            searched: false
        }
    }

    handleSearchInput = (event) => {
        this.setState({
            [event.target.name]: event.target.value
        })
   }

    handleSubmit = (event) => {
        event.preventDefault()
        this.setState({searched: this.state.search !== "" ? true : false})
        this.props.updateSearchTerm(this.state.search)
    }

    render() {
        return (
            <div className="searchbar-container">
                <form className="searchbar-form">
                    <input
                        type="search"
                        name="search"
                        value={this.state.search}
                        className="search-input"
                        placeholder="Search Restaurant Name"
                        onChange={this.handleSearchInput}
                    />
                    <button
                        type="submit"
                        className="search-submit"
                        onClick={this.handleSubmit}>
                        Click me!
                    </button>
                </form>
            </div>
        )
    }
}

SearchBar.PropTypes = {
    updateSearchTerm: PropTypes.func.isRequired
}

export default SearchBar