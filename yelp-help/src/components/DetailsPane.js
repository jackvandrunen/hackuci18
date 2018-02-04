import React from 'react'
import './DetailsPane.css'
import PropTypes from 'prop-types'

const DetailsPane = (props) => {
    if (props.loading) {
        return (
            <div className = "details-pane-container">
            {/*Loading gif*/}
            <h2>LoadingText</h2>
            </div>
        )
    } else if (props.results.length > 0) {
        return (
            <div className='details-pane-container'>
                 <div className="details-pane">
                    {/* Parse out ML response from endpoint */}
                    <h2>Please help me</h2>
                </div> 
            </div>
        )
    } else if (props.searched) {
        return (
            <div className ="details-pane-container">
                <div className="no-results-found">
                {/*Fail header text*/}
                <h2>No results found for query!</h2>
                </div>
            </div> 
        )
    } else {
        return (
            <div className ="details-pane-container">
                <h2>Right Text</h2>
            </div>
        )       
    }
}

DetailsPane.PropTypes = {
    loading: PropTypes.bool.isRequired,
}

export default DetailsPane