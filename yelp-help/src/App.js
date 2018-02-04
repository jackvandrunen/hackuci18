import React, { Component } from 'react'
import Search from  './components/Search'
import request from 'request'
import {BrowserRouter as Router, Route} from 'react-router-dom'
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
        loading: false
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
      return <Redirect to="/"/>
    } else {
        this.getSearchData(searchTerm)
    }
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
        <div>
          <Banner/>
        </div>
        <Router>
          <div>
            <Search 
              updateSearchTerm={this.updateSearchTerm}
              />
            <Route exact path="/" render = {() => (
                  <ResultsList 
                      loading={this.state.loading}
                      results={this.state.results}
                      searched={this.state.searched}
                  />
              )}/>
            <Route path="/details/" render={() => (
                  <DetailsPane
                      loading={this.state.loading}
                      results={this.state.results}
                  />
              )}/>
          </div>
        </Router>
      </div>
    );
  }
}

export default App;