import React, { Component } from 'react'
import Search from  './components/Search'
import request from 'request'
import {Link, BrowserRouter as Router, Route} from 'react-router-dom'
import './App.css';
import Banner from './components/Banner'
import ResultsList from './components/ResultsList'
import DetailsPane from './components/DetailsPane'
import {Redirect} from 'react-router'

class App extends Component {
  constructor() {
      super()

      this.state = {
        searched: false,
        results: [],
        loading: false,
        searchedItem: ''
      }
    }
  updateSearchTerm = (searchTerm) => {
    if (searchTerm.length === 0) {
      console.log("zero!")
      this.setState({
        results: [],
        loading: false,
        searched: false
      })
      return <Redirect from='/' to='/public'/>
    } else {
        console.log(searchTerm)
        this.getSearchData(searchTerm)
    }
  }

  setSelectedItem = (item) => {
      this.setState(({searchedItem:item}))
  }

getSearchData = (searchTerm) => {
  try {
      var yelp_help = this
      var options = { method: 'GET',
        url: 'http://localhost:8080/search/',
        qs: { terms: searchTerm, location: 'irvine' }
      };

    request(options, function (error, response, body) {
      if (error) throw new Error(error);
      var json = JSON.parse(body)
      var food_list = json.businesses
      yelp_help.setState({
        searched: true,
        loading: false,
        results: food_list
      })
    });
  } catch (e) {
      console.log(e)
  }
}

  render() {
    return (
      <div>
        <Banner/>
        <Router>
          <div>
            <Search 
              updateSearchTerm={this.updateSearchTerm}/>
            <Route exact path="/" render = {() => (
                  <ResultsList 
                      loading={this.state.loading}
                      results={this.state.results}
                      searched={this.state.searched}
                      itemSelect={this.setSelectedItem}
                  />
              )}/>
            <Route path="/details/:place" component={DetailsPane}/>
              )}/>
          </div>
        </Router>
      </div>
    );
  }
}

export default App;