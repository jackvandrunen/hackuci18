import React from 'react'
import './Banner.css'
import PropTypes from 'prop-types'
import banner from '../assets/MainMenuBanner.png'

class Banner extends React.Component {
    render() {
        return (
            <div className='banner-container'>
                <img src={banner} alt="Banner" className='banner-image'/>
            </div> 
        )
    }
}

export default Banner